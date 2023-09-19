from django.db import models

# Create your models here.
class SubjectCategory(models.Model):    #추후 데이터에 맞게 설정할 예정
    entire = models.CharField(max_length=200)
    philosophy = models.CharField(max_length=200)
    Religion = models.CharField(max_length=200)
    Science = models.CharField(max_length=200)
    Art = models.CharField(max_length=200)
    Language = models.CharField(max_length=200)

class Search(models.Model):
    search_id = models.IntegerField(primary_key=True)   #Autofield
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    sentence = models.TextField(null=True, default='')
    search_date = models.DateTimeField(auto_now_add=True, null=True)   #입력 시간을 기준으로 값 입력

    def __str__(self) -> str:
        return self.sentence

class Answer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    search_id = models.ForeignKey(Search, on_delete=models.CASCADE, related_name='answer_id')
    #book_id = models.ForeignKey(Book, on_delete=models.CASCADE, default='', null=True)
    answer = models.TextField(null=True, default='')

    def __str__(self):
        return self.answer
