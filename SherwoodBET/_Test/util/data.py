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
        matches = [
            ['Fc Barca', 'Sevilla'], ['Eibar', 'R Madrid'], ['Espanyol', 'Betis'], ['Granada', 'Villareal'],
            ['Las Palmas', 'A Madrid'], ['Valencia', 'Celta'], ['A Bilbao', 'Gijon'],]
        for pair in matches:
            home_team = Team.objects.get(short_name=pair[0])
            away_team = Team.objects.get(short_name=pair[1])
            deadline = datetime.strptime('Mar 1 2025  8:30PM', '%b %d %Y %I:%M%p')
            Match(home_team_obj=home_team, away_team_obj=away_team, deadline=deadline).save()
