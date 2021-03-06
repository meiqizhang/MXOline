from django.shortcuts import render
from django.views.generic.base import View
from apps.operations.forms import UserFavForm,CommentForm
from django.http import JsonResponse
from apps.operations.models import UserFavorite,CourseComments, Banner
from apps.courses.models import Course
from apps.organization.models import CourseOrg
from apps.organization.models import Teacher
class AddFavView(View):
    """
    用户收藏实现
    """
    # 先判断用户是否登录
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({
                "status":"fail",
                "msg": "用户未登录"
            })
        use_fav_form = UserFavForm(request.POST)
        if use_fav_form.is_valid():
            fav_id = use_fav_form.cleaned_data["fav_id"]
            fav_type = use_fav_form.cleaned_data["fav_type"]
            # 判断用户是否已经收藏
            existed_records = UserFavorite.objects.filter(user=request.user,fav_id=fav_id,fav_type=fav_type )
            if existed_records:
                # 收藏这条信息删除
                existed_records.delete()
                if fav_type == 1:
                    course = Course.objects.get(id = fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    cousre_org = CourseOrg.objects.get(id=fav_id)
                    cousre_org.fav_nums -= 1

                elif fav_type == 3:
                    teacher =Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()
                return JsonResponse(
                    { "status":"success",
                    "msg": "收藏"}
                )
            else:
                user_fav = UserFavorite()
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.user = request.user
                user_fav.save()
                return JsonResponse(
                    {"status": "success",
                     "msg": "已收藏"}
                )

        else:
            return JsonResponse(
                {"status": "fail",
                 "msg": "参数错误"}
            )

class CommentView(View):
    """
        用户评论
        """

    def post(self, request, *args, **kwargs):
        # 先判断用户是否登录
        if not request.user.is_authenticated:
            return JsonResponse({
                "status": "fail",
                "msg": "用户未登录"
            })
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            course = comment_form.cleaned_data["course"]
            comments = comment_form.cleaned_data["comments"]

            comment = CourseComments()
            comment.user = request.user
            comment.comments = comments
            comment.course = course
            comment.save()

            return JsonResponse({
                "status": "success",
            })
        else:
            return JsonResponse({
                "status": "success",
                "msg": '参数错误'
            })

class IndexView(View):
    def get(self, request, *args, **kwargs):
        """
        首页处理
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # banner加载
        banners = Banner.objects.all().order_by("index")[:4]

         # 公开课加载 （除去banner之外的）
        courses = Course.objects.filter(is_banner=False)[:6]

         # 小banner
        banner_courses = Course.objects.filter(is_banner=True)[:4]
        # 课程机构加载
        course_orgs = CourseOrg.objects.all()[:15]
        return render(request,'index.html',{
            "banners":banners,
            "courses":courses,
            "course_orgs":course_orgs,
            "banner_courses":banner_courses,

         })
