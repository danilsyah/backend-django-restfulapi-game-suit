import random

from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def halo(request):
    return Response({'message': 'Halo Dunia!'})


@api_view(['POST'])
def run(request):
    hand_choice = [
        'scissor',  # gunting
        'rock',  # batu
        'paper',  # kertas
    ]

    user_choice = request.data.get('user_choice')
    comp_choice = random.choice(hand_choice)

    # logic 01
    if user_choice == comp_choice:
        return Response({
            'message': 'Tie!',
            'status': True,
            'computer': comp_choice,
            'user': user_choice
        })
    # logic 02
    elif user_choice == 'rock':
        if comp_choice == 'paper':
            return Response({
                'message': 'You Lose!',
                'status': False,
                'computer': comp_choice,
                'user': user_choice
            })
        else:
            return Response({
                'message': 'You Win!',
                'status': True,
                'computer': comp_choice,
                'user': user_choice
            })
    # logic 03
    elif user_choice == 'paper':
        if comp_choice == 'scissor':
            return Response({
                'message': 'You Lose!',
                'status': False,
                'computer': comp_choice,
                'user': user_choice
            })
        else:
            return Response({
                'message': 'You Win!',
                'status': True,
                'computer': comp_choice,
                'user': user_choice
            })
    # logic 04
    elif user_choice == 'scissor':
        if comp_choice == 'rock':
            return Response({
                'message': 'You Lose!',
                'status': False,
                'computer': comp_choice,
                'user': user_choice
            })
        else:
            return Response({
                'message': 'You Win!',
                'status': True,
                'computer': comp_choice,
                'user': user_choice
            })
    # logic 05
    else:
        raise Http404
