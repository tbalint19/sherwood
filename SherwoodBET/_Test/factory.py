from App_Profile.models import Profile
from App_Game.models import Team, Match, Event, MatchEvent, Collection, MatchEventOfCollection, RaceTicket, UserTicket, Bet
from datetime import datetime

class TeamFactory:

    def create_teams(self, number):
        from collections import OrderedDict
        from pyexcel_ods import get_data
        import json
        data = get_data('_Data/raw_team_data.ods')
        created_teams = []
        for row_index in range(number):
            row = data["Sheet1"][row_index]
            stadium = row[0]
            name = row[1]
            short_name = row[2]
            team = Team(name=name, short_name=short_name, stadium=stadium)
            team.save()
            created_teams.append(team)
        return created_teams

class EventFactory:

    def create_events(self):
        names = [
            'Final result',
            'Half time result',
            '(0-1)', '(1-0)',
            'Goals (0-1 / 2-3 / 4+)',
            'Yellow cards',
            'Red cards (0, 1, 2+)']
        events = []
        for name in names:
            event = Event(name=name)
            event.save()
            events.append(event)
        return events

class MatchFactory:

    def create_matches(self, teams):
        match_datas = [teams[i:i+2] for i in range(0, len(teams), 2)]
        deadline = datetime.strptime('Jun 1 2025  1:33PM', '%b %d %Y %I:%M%p')
        created_matches = []
        for match_data in match_datas:
            match = Match(home_team_obj=match_data[0], away_team_obj=match_data[1], deadline=deadline)
            match.save()
            created_matches.append(match)
        return created_matches

class MatchEventFactory:

    def create_match_events(self, matches, events):
        match_events = []
        for match in matches:
            for event in events:
                match_event = MatchEvent(match_obj=match, event_obj=event)
                match_event.save()
                match_events.append(match_event)
        return match_events

class CollectionFactory:

    def create_match_collections(self, matches, events):
        title = "title-of-match-number-"
        intro = "intro-of-match-number-"
        collections = []
        for index, match in enumerate(matches):
            collection = Collection(number=1710100+index, title=title+str(index), intro=intro+str(index))
            for match_event in match.match_events.all():
                match_event_of_collection = MatchEventOfCollection(collection_obj=collection, match_event_obj=match_event)
                match_event_of_collection.save()
            collection.deep_analysis = True
            collection.hidden = False
            collection.playable = True
            collections.append(collection)
            collection.save()
        return collections

    def create_matches_collections(self):
        title = "title-of-league-number-"
        intro = "intro-of-league-number-"
        match_events = MatchEvent.objects.filter(event_obj__name="Final result")
        match_events_of_collections = [match_events[i:i+7] for i in range(0, len(match_events), 7)]
        collections = []
        for index, match_events_of_collection in enumerate(match_events_of_collections):
            collection = Collection(number=1710200+index, title=title+str(index), intro=intro+str(index))
            for match_event in match_events_of_collection:
                match_event_of_collection = MatchEventOfCollection(collection_obj=collection, match_event_obj=match_event)
                match_event_of_collection.save()
            collection.hidden = False
            collection.playable = True
            collections.append(collection)
            collection.save()
        return collections

class RaceTicketFactory:

    def create_race_tickets(self, collections):
        race_tickets = []
        for collection in collections:
            for boolean in [True, False]:
                for amount in [1, 10, 100]:
                    race_ticket = RaceTicket(collection_obj=collection, bet_amount=amount, is_professional=boolean)
                    race_ticket.save()
                    race_tickets.append(race_ticket)
        return race_tickets

class GameDataFactory:

    def create(self):
        teams = TeamFactory().create_teams(28)
        events = EventFactory().create_events()
        matches = MatchFactory().create_matches(teams)
        MatchEventFactory().create_match_events(matches, events)
        matches_collections = CollectionFactory().create_matches_collections()
        match_collections = CollectionFactory().create_match_collections(matches, events)
        RaceTicketFactory().create_race_tickets(match_collections + matches_collections)
