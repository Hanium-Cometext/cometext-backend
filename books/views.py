# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
#
# from .models import Book
# from .serializer import BookSerializer
# # Create your views here.
#
# #전체 책 목록 조회
# @api_view(['GET','POST'])
# def BooksAPI(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #특정 책 1개 조회
# @api_view(['GET'])
# def BookAPI(request, book_id):
#     book = get_object_or_404(Book, book_id=book_id)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# #답변과 관련된 도서 정보 조회
# @api_view(['GET'])
# def BookInfoAPI(request, answer_id):
#     book = get_object_or_404(Book, answer_id=answer_id)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)