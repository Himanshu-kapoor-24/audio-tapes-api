from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from filed.models import Song, Podcast, Audiobook
from filed.serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET','PUT', 'DELETE'])
@csrf_exempt
def file_element(request, audioFileType, audioFileID):
    if audioFileID.isdigit():
        audioFileID = int(audioFileID)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    try:
        if request.method == 'GET' and audioFileType == "song":
            if int(audioFileID) == audioFileID:
                try:
                    fileObj = Song.objects.get(pk=audioFileID)
                    serializer = SongSerializer(fileObj)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT' and audioFileType == "song":
            try:
                fileObj = Song.objects.get(pk=audioFileID)
                serializer = SongSerializer(fileObj, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE' and audioFileType == "song":
                try:
                    fileObj = Song.objects.get(pk=audioFileID)
                    fileObj.delete()
                    return HttpResponse(status=status.HTTP_200_OK)
                except:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
                
        elif request.method == 'GET' and audioFileType == "podcast":
            if int(audioFileID) == audioFileID:
                try:
                    fileObj = Podcast.objects.get(pk=audioFileID)
                    serializer = PodcastSerializer(fileObj)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT' and audioFileType == "podcast":
            try:
                fileObj = Podcast.objects.get(pk=audioFileID)
                serializer = PodcastSerializer(fileObj, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE' and audioFileType == "podcast":
                try:
                    fileObj = Podcast.objects.get(pk=audioFileID)
                    fileObj.delete()
                    return HttpResponse(status=status.HTTP_200_OK)
                except:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET' and audioFileType == "audiobook":    
            if int(audioFileID) == audioFileID:
                try:
                    fileObj = Audiobook.objects.get(pk=audioFileID)
                    serializer = AudiobookSerializer(fileObj)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT' and audioFileType == "audiobook":
            try:
                fileObj = Audiobook.objects.get(pk=audioFileID)
                serializer = AudiobookSerializer(fileObj, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE' and audioFileType == "audiobook":
                try:
                    fileObj = Audiobook.objects.get(pk=audioFileID)
                    fileObj.delete()
                    return HttpResponse(status=status.HTTP_200_OK)
                except:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
@csrf_exempt
def file_collection(request, audioFileType):
    try:
        if request.method == 'GET' and audioFileType == "song":
            file_obj = Song.objects.all()
            serializer = SongSerializer(file_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST' and audioFileType == "song":
            try:
                serializer = SongSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                    
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET' and audioFileType == "podcast":
            file_obj = Podcast.objects.all()
            serializer = PodcastSerializer(file_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'POST' and audioFileType == "podcast":
            try:
                serializer = PodcastSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                    
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET' and audioFileType == "audiobook":
            file_obj = Audiobook.objects.all()
            serializer = AudiobookSerializer(file_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST' and audioFileType == "audiobook":
            try:
                serializer = AudiobookSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                    
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            except:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    except:
        return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)