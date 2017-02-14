from django.db import models

from member.models import MyUser

'''
1. Post모델 구현 (like_users 뺴고)
2. PostLike모델 구현 (중간자 모델로 사용)
3. Post 모델의 like_users필드 구현
4. Comment모델 구현
'''


class Post(models.Model):
    author = models.ForeignKey(MyUser)
    photo = models.ImageField(
        upload_to='post', blank=True)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        MyUser,
        through='PostLike',
        related_name='like_post_set',
    )

    def __str__(self):
        return 'Post[{}]'.format(self.id)

    def toggle_like(self, user):
        # PostLike 중간자모델에서 인자로 전달된 Post, MyUser객체를 가진 row를 조회
        pl_list = PostLike.objects.filter(post=self, user=user)

        # # 현재 인자로 전달된 User가 해당 Post(self)를 좋아요 한 적이 있는지 검사
        # # if self.like_users.filter(id=user.id).exists():
        # if self.existes():
        #     # 만약에 이미 좋아요를 했을 경우 해당 내역을 삭제
        #     #PostLike.objects.filter(post=self, user=user).delete()
        #     pl_list.delete()
        # else:
        # # 아직 내역이 없을 경우 생성해준다
        # PostLike.objects.create(post=self, use=user)

        # 파이썬 삼항연산잔 (위의 if/else 문을 한줄로
        # [True일 경우 실행문 구문] if 조건문 else [False일 경우 실행할 구문
        return PostLike.objects.create(post=self, user=user) if not pl_list.exists() else pl_list.delete()

    def add_comment(self, user, content):
        return self.comment_set.create(
            user=user,
            content=content
        )

    @property
    def like_count(self):
        return self.like_user.count()

    @property
    def comment_count(self):
        return self.comment_set.count()


class Comments(models.Model):
    author = models.ForeignKey(MyUser)
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Post[{}]\'s Comment[{}], Author[{}]'.format(self)


class PostLike(models.Model):
    user = models.ForeignKey(MyUser)
    post = models.ForeignKey(Post)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('user', 'post'),
        )

    def __str__(self):
        return 'Post[{}]\'s Like[{}]'.format(
            self.Post.id,
            self.id,
            self.user_id,
        )
