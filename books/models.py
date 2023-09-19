# from django.db import models
#
# # Create your models here.
# class Book(models.Model):
#     book_id = models.IntegerField(primary_key=True, default='')
#     #answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE, default='')
#     title = models.CharField(max_length=200, default='',null=True)
#     author = models.CharField(max_length=200, default='', null=True)
#     publisher = models.CharField(max_length=100, default='', null=True)
#     subject = models.CharField(max_length=100, default='')
#     publication_date = models.DateField(default='', null=True)
#
#     def __str__(self):
#         return self.title, self.author, self.publisher, self.subject, self.publication_date
#
#     class Meta:
#         ordering = []