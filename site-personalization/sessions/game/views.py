from django.shortcuts import render
from game.models import Player, Game, PlayerGameInfo
from game.forms import PostForm, GuessForm


attempt_dict = {"attempt": 0}


def show_home(request):
    form1 = PostForm()
    if attempt_dict['attempt'] == 0:
        if request.method == 'POST':
            form1 = PostForm(request.POST)
            if form1.is_valid():
                num = form1.cleaned_data['number']
                game = Game.objects.create(number=num)
                if request.session._session_key:
                    game.relationship.create(nikname=request.session._session_key)
                else:
                    game.relationship.create(nikname="Anonim")
                return render(
                                request,
                                'home.html',
                                {"postform": form1,
                                    "num": num,
                                    'attempt': attempt_dict['attempt']},)
            else:
                return render(
                            request,
                            'home.html',
                            {"postform": form1,
                                'attempt': attempt_dict['attempt']},)
        else:
            return render(
                            request,
                            'home.html',
                            {"postform": form1,
                                'attempt': attempt_dict['attempt']},)
    else:
        new_data = attempt_dict["attempt"]
        attempt_dict["attempt"] = 0
        return render(
                        request,
                        'home.html',
                        {"postform": form1,
                            'attempt': new_data},
                            )


def guess_number(request):
    form2 = GuessForm()
    thinked_number = Game.objects.values_list('number', flat=True).last()
    if request.method == 'POST':
        form2 = GuessForm(request.POST)
        if form2.is_valid():
            num = form2.cleaned_data['second_number']
            second_number = request.session.get('second_number', num)
            attempt_add = request.session.get('attempt', 1)
            request.session['attempt'] = attempt_add+1
            attempt_dict["attempt"] = attempt_add
            if second_number == thinked_number:
                player = Player.objects.last()
                player.delete()
                game = Game.objects.last()
                game.delete()
                del request.session['attempt']
                context = {
                    'player_number': second_number,
                    'attempt': attempt_dict['attempt'],
                    'thinked_number': thinked_number,
                            }

                return render(
                        request,
                        'guess.html',
                        context
                    )
            context = {
                    "guessform": form2,
                    'player_number': second_number,
                    'thinked_number': thinked_number,
                            }
            return render(
                        request,
                        'guess.html',
                        context
                    )
        else:
            return render(
                    request,
                    'guess.html',
                    {"guessform": form2, })

    else:
        return render(
            request,
            'guess.html',
            {"guessform": form2, })
