from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Search, Answer
from .serializer import SearchSerializer, AnswerSerializer

#search: 채팅 검색. 사용자가 전송하는 부분.
#질문 생성, 조회
@api_view(['GET', 'POST'])
def SearchesAPI(request):
    if request.method == 'GET':
        searches = Search.objects.all()
        serializer = SearchSerializer(searches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#특정 질문 조회
@api_view(['GET'])
def SearchAPI(request, search_id):
    search = get_object_or_404(Search, search_id=search_id)
    serializer = SearchSerializer(search)
    return Response(serializer.data, status=status.HTTP_200_OK)


#특정 질문 삭제
@api_view(['DELETE'])
def SearchDeleteAPI(request, search_id):
    search = get_object_or_404(Search, search_id=search_id)
    search.delete()
    serializer = SearchSerializer(search)
    return Response(status=status.HTTP_201_CREATED)

#전체 답변 조회
@api_view(['GET','POST'])
def AnswersAPI(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#특정 질문에 대한 답변 1개 조회
@api_view(['GET'])
def AnswerAPI(request, answer_id, search_id):
    answer = get_object_or_404(Answer, answer_id=answer_id, search_id=search_id)
    serializer = AnswerSerializer(answer)
    return Response(serializer.data, status=status.HTTP_200_OK)

# #특정 질문에 대한 답변 전체 조회
# @api_view(['GET'])
# def AnswersBySearchAPI(request, search_id):
#         answers = get_object_or_404(Answer, search_id=search_id)
#         serializer = AnswerSerializer(answers, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#특정 답변 관련 책 정보 조회

# @api_view(['GET'])
# def get_sentences(request):
#     if request.query_params:
#         searches = Search.objects.filter(**request.query_params.dict())
#     else:
#         searches = Search.objects.all()
#
#     if searches:
#         serializer = SearchSerializer(searches, many=True)
#         return Response(serializer.data)
#     else:
#         return  Response(status=status.HTTP_404_NOT_FOUND)
