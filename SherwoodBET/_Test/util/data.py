from App_Game.models import Team, Event, Match, MatchEvent, Collection, MatchEventOfCollection, RaceTicket
from datetime import datetime

class TestData:

    teams = [
        ['Fc Barca', 'FC Barcelona', 'Camp Nou'],
        ['R Madrid', 'Real Madrid', 'Bernabeu'],
        ['A Madrid', 'Atletico Madrid', 'Calderon'],
        ['Sevilla', 'Sevilla', 'Pizjuan'],
        ['Villareal', 'Villareal', 'Madrigal'],
        ['R Sociedad', 'Real Sociedad', 'Anoeta'],
        ['A Bilbao', 'Athletic Bilbao', 'San Mames'],
        ['Eibar', 'Eibar', 'Ipurua'],
        ['Espanyol', 'Espanyol', 'El-Prat'],
        ['Malaga', 'Malaga', 'Rosaleda'],
        ['Celta', 'Celta Vigo', 'Balaidos'],
        ['Valencia', 'Valencia', 'Mestalla'],
        ['Deportivo', 'Deportivo la Coruna', 'Riazor'],
        ['Alaves', 'Alaves', 'Mendizorrotza'],
        ['Las Palmas', 'Las Palmas', 'Gran Canaria'],
        ['Betis', 'Real Betis', 'Villamarín'],
        ['Leganes', 'Leganes', 'Butarque'],
        ['Gijon', 'Sporting Gijon', 'Molinón'],
        ['Osasuna', 'Osasuna', 'El Sadar'],
        ['Granada', 'Granada', 'Cármenes']
    ]

    events = [
        'Final result',
        'Half time result',
        '(0-1)', '(1-0)',
        'Goals (0-1 / 2-3 / 4+)',
        'Yellow cards',
        'Red cards (0, 1, 2+)'
    ]

    def create_teams(self):
        for data in self.__class__.teams:
            Team(name=data[1], short_name=data[0], stadium=data[2]).save()

    def create_events(self):
        for data in self.__class__.events:
            Event(name=data).save()

    def create_matches(self):
        barca = Team.objects.get(short_name="Fc Barca")
        real = Team.objects.get(short_name="R Madrid")
        deadline = datetime.strptime('Jun 1 2025  8:30PM', '%b %d %Y %I:%M%p')
        Match(home_team_obj=barca, away_team_obj=real, deadline=deadline).save()
