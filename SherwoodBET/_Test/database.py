from App_Game.models import Team, Event, Match, MatchEvent, Collection, MatchEventOfCollection, RaceTicket
from datetime import datetime

def populate_data():

    barca = Team(name="Barcelona", short_name="FC Barca", stadium="Camp Nou"); barca.save();
    real = Team(name="Real Madrid", short_name="R Madrid", stadium="Santiago Bernabéu"); real.save();
    atletico = Team(name="Atlético Madrid", short_name="A Madrid", stadium="Vicente Calderón"); atletico.save();
    sevilla = Team(name="Sevilla", short_name="Sevilla", stadium="Ramón Sánchez-Pizjuán"); sevilla.save();
    villareal = Team(name="Villarreal", short_name="Villarreal", stadium="El Madrigal"); villareal.save();
    sociedad = Team(name="Real Sociedad", short_name="R Sociedad", stadium="Anoeta"); sociedad.save();
    bilbao = Team(name="Athletic Bilbao", short_name="A Bilbao", stadium="San Mamés"); bilbao.save();
    eibar = Team(name="Eibar", short_name="Eibar", stadium="Municipal de Ipurua"); eibar.save();
    espanyol = Team(name="Espanyol", short_name="Espanyol", stadium="Cornellà-El Prat"); espanyol.save();
    malaga = Team(name="Malaga", short_name="Malaga", stadium="La Rosaleda"); malaga.save();
    celta = Team(name="Celta de Vigo", short_name="Celta", stadium="Balaídos"); celta.save();
    valencia = Team(name="Valencia", short_name="Valencia", stadium="Mestalla"); valencia.save();
    depor = Team(name="Deportivo La Coruña", short_name="Depor", stadium="Riazor"); depor.save();
    alaves = Team(name="Alaves", short_name="Alaves", stadium="Mendizorroza"); alaves.save();
    lpalmas = Team(name="Las Palmas", short_name="Las Palmas", stadium="Estadio Gran Canaria"); lpalmas.save();
    betis = Team(name="Betis", short_name="Betis", stadium="Villamarín"); betis.save();
    leganes = Team(name="Leganes", short_name="Leganes", stadium="Butarque"); leganes.save();
    gijon = Team(name="Sporting de Gijón", short_name="Gijón", stadium="Molinón"); gijon.save();
    osasuna = Team(name="Osasuna", short_name="Osasuna", stadium="El Sadar"); osasuna.save();
    granada = Team(name="Granada", short_name="Granada", stadium="Cármenes"); granada.save();

    chelsea = Team(name="Chelsea", short_name="Chelsea", stadium="Stamford Bridge	"); chelsea.save();
    tottenham = Team(name="Tottenham", short_name="Tottenham", stadium="White Hart Lane"); tottenham.save();
    liverpool = Team(name="Liverpool", short_name="Liverpool", stadium="Anfield"); liverpool.save();
    mancity = Team(name="Manchester City", short_name="Man City", stadium="The Etihad"); mancity.save();
    arsenal = Team(name="Arsenal", short_name="Arsenal", stadium="The Emirates"); arsenal.save();
    manutd = Team(name="Manchester United", short_name="Man Utd", stadium="Old Trafford"); manutd.save();
    everton = Team(name="Everton", short_name="Everton", stadium="Goodison Park"); everton.save();
    soton = Team(name="Southampton", short_name="Southampton", stadium="St Mary's Stadium"); soton.save();
    leicester = Team(name="Leicester City", short_name="Leicester", stadium="King Power Stadium"); leicester.save();
    watford = Team(name="Watford", short_name="Watford", stadium="Vicarage Road"); watford.save();
    bmouth = Team(name="Bournemouth", short_name="Bournemouth", stadium="Vitality Stadium"); bmouth.save();
    stoke = Team(name="Stoke", short_name="Stoke", stadium="Britannia Stadium"); stoke.save();
    swansea = Team(name="Swansea", short_name="Swansea", stadium="Liberty Stadium"); swansea.save();
    palace = Team(name="Crystal Palace", short_name="C Palace", stadium="Selhurst Park"); palace.save();
    westham = Team(name="West Ham United", short_name="West Ham", stadium="Olympic Stadium London"); westham.save();
    westbrom = Team(name="West Brom", short_name="West Brom", stadium="The Hawthorns"); westbrom.save();
    hull = Team(name="Hull City", short_name="Hull City", stadium="KC Stadium"); hull.save();
    sunderland = Team(name="Sunderland", short_name="Sunderland", stadium="Stadium of Light"); sunderland.save();
    mbrough = Team(name="Middlesbrough", short_name="Middlesbrough", stadium="Riverside Stadium"); mbrough.save();
    burnley = Team(name="Burnley", short_name="Burnley", stadium="Turf Moor"); burnley.save();

    bayern = Team(name="Bayern Munich", short_name="B Munchen", stadium="Allianz Arena"); bayern.save();
    redbull = Team(name="RB Leipzig", short_name="RB Leipzig", stadium="Red Bull Arena"); redbull.save();
    dortmund = Team(name="Borussia Dortmund", short_name="Dortmund", stadium="Signal Iduna Park"); dortmund.save();
    hoffenheim = Team(name="TSG 1899 Hoffenheim", short_name="Hoffenheim", stadium="Rhein-Neckar Arena"); hoffenheim.save();
    koln = Team(name="1. FC Köln", short_name="Köln", stadium="RheinEnergieStadion"); koln.save();
    hertha = Team(name="Hertha BSC", short_name="Hertha", stadium="Olympiastadion Berlin"); hertha.save();
    frankfurt = Team(name="Eintracht Frankfurt", short_name="Frankfurt", stadium="Commerzbank Arena"); frankfurt.save();
    bayer = Team(name="Bayer Leverkusen", short_name="Bayer", stadium="BayArena"); bayer.save();
    wolfsburg = Team(name="VFL Wolfsburg", short_name="Wolfsburg", stadium="Volkswagen Arena"); wolfsburg.save();
    hamburg = Team(name="Hamburger SV", short_name="Hamburg", stadium="Imtech Arena"); hamburg.save();
    darmstadt = Team(name="SV Darmstadt 98", short_name="Darmstadt", stadium="Stadion am Böllenfalltor"); darmstadt.save();
    ingolstadt = Team(name="Ingolstadt", short_name="Ingolstadt", stadium="Audi Sportpark"); ingolstadt.save();
    schalke = Team(name="FC Schalke 04", short_name="Schalke", stadium="Veltins-Arena"); schalke.save();
    mgladbach = Team(name="Borussia Mönchengladbach", short_name="M.Gladbach", stadium="Stadion im Borussia-Park"); mgladbach.save();
    augsburg = Team(name="FC Augsburg", short_name="Augsburg", stadium="WWK Arena"); augsburg.save();
    mainz = Team(name="1. FSV Mainz 05", short_name="Mainz", stadium="Coface Arena"); mainz.save();
    werder = Team(name="Werder Bremen", short_name="Werder", stadium="Weserstadion"); werder.save();
    freiburg = Team(name="SC Freiburg", short_name="Freiburg", stadium="Dreisamstadion"); freiburg.save();

    result = Event(name="Final result"); result.save();
    halftime = Event(name="Half time result"); halftime.save();
    homehandy = Event(name="(0-1) handicap"); homehandy.save();
    awayhandy = Event(name="(1-0) handicap"); awayhandy.save();
    goals = Event(name="0-1/2-3/4+ goals"); goals.save();
    corners = Event(name="0-5/6-11/12+ corners"); corners.save();
    yellows = Event(name="0-5/6-11/12+ yellow cards"); yellows.save();
    reds = Event(name="0/1/2+ red cards"); reds.save();

    l = "Primera Division"; r = "1st round"
    d1 = datetime.strptime('Sep 3 2018  6:00PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 4 2018  7:30PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 5 2018  9:00PM', '%b %d %Y %I:%M%p')
    bilbao_barca = Match(home_team_obj=bilbao, away_team_obj=barca, league=l, round=r, deadline=d1); bilbao_barca.save()
    real_leganes = Match(home_team_obj=real, away_team_obj=leganes, league=l, round=r, deadline=d1); real_leganes.save()
    espanyol_villareal = Match(home_team_obj=espanyol, away_team_obj=villareal, league=l, round=r, deadline=d2); espanyol_villareal.save()
    atletico_eibar = Match(home_team_obj=atletico, away_team_obj=eibar, league=l, round=r, deadline=d2); atletico_eibar.save()
    granada_sevilla = Match(home_team_obj=granada, away_team_obj=sevilla, league=l, round=r, deadline=d2); granada_sevilla.save()
    celta_valencia = Match(home_team_obj=celta, away_team_obj=valencia, league=l, round=r, deadline=d2); celta_valencia.save()
    depor_malaga = Match(home_team_obj=depor, away_team_obj=malaga, league=l, round=r, deadline=d3); depor_malaga.save()

    l = "Premier League"; r = "4th round"
    d1 = datetime.strptime('Sep 4 2018  9:30PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 5 2018  4:00PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 6 2018  8:45PM', '%b %d %Y %I:%M%p')
    chelsea_sunderland = Match(home_team_obj=chelsea, away_team_obj=sunderland, league=l, round=r, deadline=d1); chelsea_sunderland.save()
    manutd_westham = Match(home_team_obj=manutd, away_team_obj=westham, league=l, round=r, deadline=d1); manutd_westham.save()
    everton_swansea = Match(home_team_obj=everton, away_team_obj=swansea, league=l, round=r, deadline=d1); everton_swansea.save()
    soton_arsenal = Match(home_team_obj=soton, away_team_obj=arsenal, league=l, round=r, deadline=d1); soton_arsenal.save()
    liverpool_mancity = Match(home_team_obj=liverpool, away_team_obj=mancity, league=l, round=r, deadline=d2); liverpool_mancity.save()
    tottenham_westbrom = Match(home_team_obj=tottenham, away_team_obj=westbrom, league=l, round=r, deadline=d2); tottenham_westbrom.save()
    leicester_hull = Match(home_team_obj=leicester, away_team_obj=hull, league=l, round=r, deadline=d3); leicester_hull.save()

    l = "Bundesliga"; r = "2nd round"
    d1 = datetime.strptime('Sep 4 2018  3:30PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 4 2018  6:30PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 5 2018  5:30PM', '%b %d %Y %I:%M%p')
    bayern_wolfsburg = Match(home_team_obj=bayern, away_team_obj=wolfsburg, league=l, round=r, deadline=d1); bayern_wolfsburg.save()
    augsburg_hertha = Match(home_team_obj=hertha, away_team_obj=augsburg, league=l, round=r, deadline=d1); augsburg_hertha.save()
    bayer_redbull = Match(home_team_obj=bayer, away_team_obj=redbull, league=l, round=r, deadline=d1); bayer_redbull.save()
    hoffenheim_hamburg = Match(home_team_obj=hoffenheim, away_team_obj=hamburg, league=l, round=r, deadline=d1); hoffenheim_hamburg.save()
    werder_dortmund = Match(home_team_obj=werder, away_team_obj=dortmund, league=l, round=r, deadline=d2); werder_dortmund.save()
    koln_schalke = Match(home_team_obj=koln, away_team_obj=schalke, league=l, round=r, deadline=d3); koln_schalke.save()
    frankfurt_darmstadt = Match(home_team_obj=frankfurt, away_team_obj=darmstadt, league=l, round=r, deadline=d3); frankfurt_darmstadt.save()

    bilbao_barca_result = MatchEvent(match_obj=bilbao_barca, event_obj=result); bilbao_barca_result.save()
    real_leganes_result = MatchEvent(match_obj=real_leganes, event_obj=result); real_leganes_result.save()
    espanyol_villareal_result = MatchEvent(match_obj=espanyol_villareal, event_obj=result); espanyol_villareal_result.save()
    atletico_eibar_result = MatchEvent(match_obj=atletico_eibar, event_obj=result); atletico_eibar_result.save()
    granada_sevilla_result = MatchEvent(match_obj=granada_sevilla, event_obj=result); granada_sevilla_result.save()
    celta_valencia_result = MatchEvent(match_obj=celta_valencia, event_obj=result); celta_valencia_result.save()
    depor_malaga_result = MatchEvent(match_obj=depor_malaga, event_obj=result); depor_malaga_result.save()

    chelsea_sunderland_result = MatchEvent(match_obj=chelsea_sunderland, event_obj=result); chelsea_sunderland_result.save()
    manutd_westham_result = MatchEvent(match_obj=manutd_westham, event_obj=result); manutd_westham_result.save()
    everton_swansea_result = MatchEvent(match_obj=everton_swansea, event_obj=result); everton_swansea_result.save()
    soton_arsenal_result = MatchEvent(match_obj=soton_arsenal, event_obj=result); soton_arsenal_result.save()
    liverpool_mancity_result = MatchEvent(match_obj=liverpool_mancity, event_obj=result); liverpool_mancity_result.save()
    tottenham_westbrom_result = MatchEvent(match_obj=tottenham_westbrom, event_obj=result); tottenham_westbrom_result.save()
    leicester_hull_result = MatchEvent(match_obj=leicester_hull, event_obj=result); leicester_hull_result.save()

    bayern_wolfsburg_result = MatchEvent(match_obj=bayern_wolfsburg, event_obj=result); bayern_wolfsburg_result.save()
    augsburg_hertha_result = MatchEvent(match_obj=augsburg_hertha, event_obj=result); augsburg_hertha_result.save()
    bayer_redbull_result = MatchEvent(match_obj=bayer_redbull, event_obj=result); bayer_redbull_result.save()
    hoffenheim_hamburg_result = MatchEvent(match_obj=hoffenheim_hamburg, event_obj=result); hoffenheim_hamburg_result.save()
    werder_dortmund_result = MatchEvent(match_obj=werder_dortmund, event_obj=result); werder_dortmund_result.save()
    koln_schalke_result = MatchEvent(match_obj=koln_schalke, event_obj=result); koln_schalke_result.save()
    frankfurt_darmstadt_result = MatchEvent(match_obj=frankfurt_darmstadt, event_obj=result); frankfurt_darmstadt_result.save()

    bilbao_barca_halftime = MatchEvent(match_obj=bilbao_barca, event_obj=halftime); bilbao_barca_halftime.save()
    bilbao_barca_homehandy = MatchEvent(match_obj=bilbao_barca, event_obj=homehandy); bilbao_barca_homehandy.save()
    bilbao_barca_awayhandy = MatchEvent(match_obj=bilbao_barca, event_obj=awayhandy); bilbao_barca_awayhandy.save()
    bilbao_barca_goals = MatchEvent(match_obj=bilbao_barca, event_obj=goals); bilbao_barca_goals.save()
    bilbao_barca_yellows = MatchEvent(match_obj=bilbao_barca, event_obj=yellows); bilbao_barca_yellows.save()
    bilbao_barca_reds = MatchEvent(match_obj=bilbao_barca, event_obj=reds); bilbao_barca_reds.save()

    liverpool_mancity_halftime = MatchEvent(match_obj=liverpool_mancity, event_obj=halftime); liverpool_mancity_halftime.save()
    liverpool_mancity_homehandy = MatchEvent(match_obj=liverpool_mancity, event_obj=homehandy); liverpool_mancity_homehandy.save()
    liverpool_mancity_awayhandy = MatchEvent(match_obj=liverpool_mancity, event_obj=awayhandy); liverpool_mancity_awayhandy.save()
    liverpool_mancity_goals = MatchEvent(match_obj=liverpool_mancity, event_obj=goals); liverpool_mancity_goals.save()
    liverpool_mancity_yellows = MatchEvent(match_obj=liverpool_mancity, event_obj=yellows); liverpool_mancity_yellows.save()
    liverpool_mancity_reds = MatchEvent(match_obj=liverpool_mancity, event_obj=reds); liverpool_mancity_reds.save()

    werder_dortmund_halftime = MatchEvent(match_obj=werder_dortmund, event_obj=halftime); werder_dortmund_halftime.save()
    werder_dortmund_homehandy = MatchEvent(match_obj=werder_dortmund, event_obj=homehandy); werder_dortmund_homehandy.save()
    werder_dortmund_awayhandy = MatchEvent(match_obj=werder_dortmund, event_obj=awayhandy); werder_dortmund_awayhandy.save()
    werder_dortmund_goals = MatchEvent(match_obj=werder_dortmund, event_obj=goals); werder_dortmund_goals.save()
    werder_dortmund_yellows = MatchEvent(match_obj=werder_dortmund, event_obj=yellows); werder_dortmund_yellows.save()
    werder_dortmund_reds = MatchEvent(match_obj=werder_dortmund, event_obj=reds); werder_dortmund_reds.save()

    primera_division_1 = Collection(number=1725101, title="PD 16/17 1 matches", intro="placeholder"); primera_division_1.save()
    premier_league_1 = Collection(number=1725102, title="PL 16/17 4 matches", intro="placeholder"); premier_league_1.save()
    bundesliga_1 = Collection(number=1725103, title="PD 16/17 2 matches", intro="placeholder"); bundesliga_1.save()

    spanish_derby_1 = Collection(number=1725201, title="PD 16/17 1 derby", intro="placeholder", is_deep_analysis=True); spanish_derby_1.save()
    english_derby_1 = Collection(number=1725202, title="PD 16/17 4 derby", intro="placeholder", is_deep_analysis=True); english_derby_1.save()
    german_derby_1 = Collection(number=1725203, title="PD 16/17 2 derby", intro="placeholder", is_deep_analysis=True); german_derby_1.save()

    offer = [
        {
            'collection': primera_division_1,
            'match_events': [
                bilbao_barca_result,
                real_leganes_result,
                espanyol_villareal_result,
                atletico_eibar_result,
                granada_sevilla_result,
                celta_valencia_result,
                depor_malaga_result
            ]
        },
        {
            'collection': premier_league_1,
            'match_events': [
                chelsea_sunderland_result,
                manutd_westham_result,
                everton_swansea_result,
                soton_arsenal_result,
                liverpool_mancity_result,
                tottenham_westbrom_result,
                leicester_hull_result
            ]
        },
        {
            'collection': bundesliga_1,
            'match_events': [
                bayern_wolfsburg_result,
                augsburg_hertha_result,
                bayer_redbull_result,
                hoffenheim_hamburg_result,
                werder_dortmund_result,
                koln_schalke_result,
                frankfurt_darmstadt_result
            ]
        },
        {
            'collection': spanish_derby_1,
            'match_events': [
                bilbao_barca_result,
                bilbao_barca_halftime,
                bilbao_barca_homehandy,
                bilbao_barca_awayhandy,
                bilbao_barca_goals,
                bilbao_barca_yellows,
                bilbao_barca_reds
            ]
        },
        {
            'collection': english_derby_1,
            'match_events': [
                liverpool_mancity_result,
                liverpool_mancity_halftime,
                liverpool_mancity_homehandy,
                liverpool_mancity_awayhandy,
                liverpool_mancity_goals,
                liverpool_mancity_yellows,
                liverpool_mancity_reds
            ]
        },
        {
            'collection': german_derby_1,
            'match_events': [
                werder_dortmund_result,
                werder_dortmund_halftime,
                werder_dortmund_homehandy,
                werder_dortmund_awayhandy,
                werder_dortmund_goals,
                werder_dortmund_yellows,
                werder_dortmund_reds
            ]
        }
    ]

    for data in offer:
        collection = data['collection']
        match_events = data['match_events']
        for match_event in match_events:
            MatchEventOfCollection(match_event_obj=match_event, collection_obj=collection).save()
        for boolean in [True, False]:
            for amount in [1, 10, 100]:
                RaceTicket(collection_obj=collection, bet_amount=amount, is_professional=boolean).save()

    l = "Primera Division"; r = "2nd round"
    d1 = datetime.strptime('Sep 10 2018  6:00PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 11 2018  7:30PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 12 2018  9:00PM', '%b %d %Y %I:%M%p')
    barca_real = Match(home_team_obj=barca, away_team_obj=real, league=l, round=r, deadline=d1); barca_real.save()
    leganes_bilbao = Match(home_team_obj=leganes, away_team_obj=bilbao, league=l, round=r, deadline=d1); leganes_bilbao.save()
    eibar_espanyol = Match(home_team_obj=eibar, away_team_obj=espanyol, league=l, round=r, deadline=d2); eibar_espanyol.save()
    villareal_atletico = Match(home_team_obj=villareal, away_team_obj=atletico, league=l, round=r, deadline=d2); villareal_atletico.save()
    malaga_granada = Match(home_team_obj=malaga, away_team_obj=granada, league=l, round=r, deadline=d2); malaga_granada.save()
    celta_depor = Match(home_team_obj=celta, away_team_obj=depor, league=l, round=r, deadline=d2); celta_depor.save()
    valencia_sevilla = Match(home_team_obj=valencia, away_team_obj=sevilla, league=l, round=r, deadline=d3); valencia_sevilla.save()

    l = "Premier League"; r = "5th round"
    d1 = datetime.strptime('Sep 11 2018  9:30PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 12 2018  4:00PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 13 2018  8:45PM', '%b %d %Y %I:%M%p')
    sunderland_manutd = Match(home_team_obj=sunderland, away_team_obj=manutd, league=l, round=r, deadline=d1); sunderland_manutd.save()
    westham_chelsea = Match(home_team_obj=westham, away_team_obj=chelsea, league=l, round=r, deadline=d1); westham_chelsea.save()
    swansea_soton = Match(home_team_obj=swansea, away_team_obj=soton, league=l, round=r, deadline=d1); swansea_soton.save()
    arsenal_everton = Match(home_team_obj=arsenal, away_team_obj=everton, league=l, round=r, deadline=d1); arsenal_everton.save()
    hull_mancity = Match(home_team_obj=hull, away_team_obj=mancity, league=l, round=r, deadline=d2); hull_mancity.save()
    westbrom_leicester = Match(home_team_obj=westbrom, away_team_obj=leicester, league=l, round=r, deadline=d2); westbrom_leicester.save()
    tottenham_liverpool = Match(home_team_obj=tottenham, away_team_obj=liverpool, league=l, round=r, deadline=d3); tottenham_liverpool.save()

    l = "Bundesliga"; r = "3rd round"
    d1 = datetime.strptime('Sep 11 2018  3:30PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 11 2018  6:30PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 12 2018  5:30PM', '%b %d %Y %I:%M%p')
    wolfsburg_augsburg = Match(home_team_obj=wolfsburg, away_team_obj=augsburg, league=l, round=r, deadline=d1); wolfsburg_augsburg.save()
    hertha_bayern = Match(home_team_obj=hertha, away_team_obj=bayern, league=l, round=r, deadline=d1); hertha_bayern.save()
    redbull_hoffenheim = Match(home_team_obj=redbull, away_team_obj=hoffenheim, league=l, round=r, deadline=d1); redbull_hoffenheim.save()
    hamburg_bayer = Match(home_team_obj=hamburg, away_team_obj=bayer, league=l, round=r, deadline=d1); hamburg_bayer.save()
    schalke_darmstadt = Match(home_team_obj=schalke, away_team_obj=darmstadt, league=l, round=r, deadline=d2); schalke_darmstadt.save()
    koln_werder = Match(home_team_obj=koln, away_team_obj=werder, league=l, round=r, deadline=d3); koln_werder.save()
    dortmund_frankfurt = Match(home_team_obj=dortmund, away_team_obj=frankfurt, league=l, round=r, deadline=d3); dortmund_frankfurt.save()

    barca_real_result = MatchEvent(match_obj=barca_real, event_obj=result); barca_real_result.save()
    leganes_bilbao_result = MatchEvent(match_obj=leganes_bilbao, event_obj=result); leganes_bilbao_result.save()
    eibar_espanyol_result = MatchEvent(match_obj=eibar_espanyol, event_obj=result); eibar_espanyol_result.save()
    villareal_atletico_result = MatchEvent(match_obj=villareal_atletico, event_obj=result); villareal_atletico_result.save()
    malaga_granada_result = MatchEvent(match_obj=malaga_granada, event_obj=result); malaga_granada_result.save()
    celta_depor_result = MatchEvent(match_obj=celta_depor, event_obj=result); celta_depor_result.save()
    valencia_sevilla_result = MatchEvent(match_obj=valencia_sevilla, event_obj=result); valencia_sevilla_result.save()

    sunderland_manutd_result = MatchEvent(match_obj=sunderland_manutd, event_obj=result); sunderland_manutd_result.save()
    westham_chelsea_result = MatchEvent(match_obj=westham_chelsea, event_obj=result); westham_chelsea_result.save()
    swansea_soton_result = MatchEvent(match_obj=swansea_soton, event_obj=result); swansea_soton_result.save()
    arsenal_everton_result = MatchEvent(match_obj=arsenal_everton, event_obj=result); arsenal_everton_result.save()
    hull_mancity_result = MatchEvent(match_obj=hull_mancity, event_obj=result); hull_mancity_result.save()
    westbrom_leicester_result = MatchEvent(match_obj=westbrom_leicester, event_obj=result); westbrom_leicester_result.save()
    tottenham_liverpool_result = MatchEvent(match_obj=tottenham_liverpool, event_obj=result); tottenham_liverpool_result.save()

    wolfsburg_augsburg_result = MatchEvent(match_obj=wolfsburg_augsburg, event_obj=result); wolfsburg_augsburg_result.save()
    hertha_bayern_result = MatchEvent(match_obj=hertha_bayern, event_obj=result); hertha_bayern_result.save()
    redbull_hoffenheim_result = MatchEvent(match_obj=redbull_hoffenheim, event_obj=result); redbull_hoffenheim_result.save()
    hamburg_bayer_result = MatchEvent(match_obj=hamburg_bayer, event_obj=result); hamburg_bayer_result.save()
    schalke_darmstadt_result = MatchEvent(match_obj=schalke_darmstadt, event_obj=result); schalke_darmstadt_result.save()
    koln_werder_result = MatchEvent(match_obj=koln_werder, event_obj=result); koln_werder_result.save()
    dortmund_frankfurt_result = MatchEvent(match_obj=dortmund_frankfurt, event_obj=result); dortmund_frankfurt_result.save()

    barca_real_halftime = MatchEvent(match_obj=barca_real, event_obj=halftime); barca_real_halftime.save()
    barca_real_homehandy = MatchEvent(match_obj=barca_real, event_obj=homehandy); barca_real_homehandy.save()
    barca_real_awayhandy = MatchEvent(match_obj=barca_real, event_obj=awayhandy); barca_real_awayhandy.save()
    barca_real_goals = MatchEvent(match_obj=barca_real, event_obj=goals); barca_real_goals.save()
    barca_real_yellows = MatchEvent(match_obj=barca_real, event_obj=yellows); barca_real_yellows.save()
    barca_real_reds = MatchEvent(match_obj=barca_real, event_obj=reds); barca_real_reds.save()

    tottenham_liverpool_halftime = MatchEvent(match_obj=tottenham_liverpool, event_obj=halftime); tottenham_liverpool_halftime.save()
    tottenham_liverpool_homehandy = MatchEvent(match_obj=tottenham_liverpool, event_obj=homehandy); tottenham_liverpool_homehandy.save()
    tottenham_liverpool_awayhandy = MatchEvent(match_obj=tottenham_liverpool, event_obj=awayhandy); tottenham_liverpool_awayhandy.save()
    tottenham_liverpool_goals = MatchEvent(match_obj=tottenham_liverpool, event_obj=goals); tottenham_liverpool_goals.save()
    tottenham_liverpool_yellows = MatchEvent(match_obj=tottenham_liverpool, event_obj=yellows); tottenham_liverpool_yellows.save()
    tottenham_liverpool_reds = MatchEvent(match_obj=tottenham_liverpool, event_obj=reds); tottenham_liverpool_reds.save()

    hertha_bayern_halftime = MatchEvent(match_obj=hertha_bayern, event_obj=halftime); hertha_bayern_halftime.save()
    hertha_bayern_homehandy = MatchEvent(match_obj=hertha_bayern, event_obj=homehandy); hertha_bayern_homehandy.save()
    hertha_bayern_awayhandy = MatchEvent(match_obj=hertha_bayern, event_obj=awayhandy); hertha_bayern_awayhandy.save()
    hertha_bayern_goals = MatchEvent(match_obj=hertha_bayern, event_obj=goals); hertha_bayern_goals.save()
    hertha_bayern_yellows = MatchEvent(match_obj=hertha_bayern, event_obj=yellows); hertha_bayern_yellows.save()
    hertha_bayern_reds = MatchEvent(match_obj=hertha_bayern, event_obj=reds); hertha_bayern_reds.save()

    primera_division_2 = Collection(number=1726101, title="PD 16/17 2 matches", intro="placeholder"); primera_division_2.save()
    premier_league_2 = Collection(number=1726102, title="PL 16/17 5 matches", intro="placeholder"); premier_league_2.save()
    bundesliga_2 = Collection(number=1726103, title="PD 16/17 3 matches", intro="placeholder"); bundesliga_2.save()

    spanish_derby_2 = Collection(number=1726201, title="PD 16/17 2 derby", intro="placeholder", is_deep_analysis=True); spanish_derby_2.save()
    english_derby_2 = Collection(number=1726202, title="PD 16/17 5 derby", intro="placeholder", is_deep_analysis=True); english_derby_2.save()
    german_derby_2 = Collection(number=1726203, title="PD 16/17 3 derby", intro="placeholder", is_deep_analysis=True); german_derby_2.save()

    offer = [
        {
            'collection': primera_division_2,
            'match_events': [
                barca_real_result,
                leganes_bilbao_result,
                eibar_espanyol_result,
                villareal_atletico_result,
                malaga_granada_result,
                celta_depor_result,
                valencia_sevilla_result
            ]
        },
        {
            'collection': premier_league_2,
            'match_events': [
                sunderland_manutd_result,
                westham_chelsea_result,
                swansea_soton_result,
                arsenal_everton_result,
                hull_mancity_result,
                westbrom_leicester_result,
                tottenham_liverpool_result
            ]
        },
        {
            'collection': bundesliga_2,
            'match_events': [
                wolfsburg_augsburg_result,
                hertha_bayern_result,
                redbull_hoffenheim_result,
                hamburg_bayer_result,
                schalke_darmstadt_result,
                koln_werder_result,
                dortmund_frankfurt_result
            ]
        },
        {
            'collection': spanish_derby_2,
            'match_events': [
                barca_real_result,
                barca_real_halftime,
                barca_real_homehandy,
                barca_real_awayhandy,
                barca_real_goals,
                barca_real_yellows,
                barca_real_reds
            ]
        },
        {
            'collection': english_derby_2,
            'match_events': [
                tottenham_liverpool_result,
                tottenham_liverpool_halftime,
                tottenham_liverpool_homehandy,
                tottenham_liverpool_awayhandy,
                tottenham_liverpool_goals,
                tottenham_liverpool_yellows,
                tottenham_liverpool_reds
            ]
        },
        {
            'collection': german_derby_2,
            'match_events': [
                hertha_bayern_result,
                hertha_bayern_halftime,
                hertha_bayern_homehandy,
                hertha_bayern_awayhandy,
                hertha_bayern_goals,
                hertha_bayern_yellows,
                hertha_bayern_reds
            ]
        }
    ]

    for data in offer:
        collection = data['collection']
        match_events = data['match_events']
        for match_event in match_events:
            MatchEventOfCollection(match_event_obj=match_event, collection_obj=collection).save()
        for boolean in [True, False]:
            for amount in [1, 10, 100]:
                RaceTicket(collection_obj=collection, bet_amount=amount, is_professional=boolean).save()

    l = "Primera Division"; r = "3rd round"
    d1 = datetime.strptime('Sep 17 2018  6:00PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 18 2018  7:30PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 19 2018  9:00PM', '%b %d %Y %I:%M%p')
    espanyol_barca = Match(home_team_obj=espanyol, away_team_obj=barca, league=l, round=r, deadline=d1); espanyol_barca.save()
    real_eibar = Match(home_team_obj=real, away_team_obj=eibar, league=l, round=r, deadline=d1); real_eibar.save()
    bilbao_villareal = Match(home_team_obj=bilbao, away_team_obj=villareal, league=l, round=r, deadline=d2); bilbao_villareal.save()
    atletico_leganes = Match(home_team_obj=atletico, away_team_obj=leganes, league=l, round=r, deadline=d2); atletico_leganes.save()
    granada_celta = Match(home_team_obj=granada, away_team_obj=celta, league=l, round=r, deadline=d2); granada_celta.save()
    depor_valencia = Match(home_team_obj=depor, away_team_obj=valencia, league=l, round=r, deadline=d2); depor_valencia.save()
    malaga_sevilla = Match(home_team_obj=malaga, away_team_obj=sevilla, league=l, round=r, deadline=d3); malaga_sevilla.save()

    l = "Premier League"; r = "6th round"
    d1 = datetime.strptime('Sep 18 2018  9:30PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 19 2018  4:00PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 20 2018  8:45PM', '%b %d %Y %I:%M%p')
    manutd_swansea = Match(home_team_obj=manutd, away_team_obj=swansea, league=l, round=r, deadline=d1); manutd_swansea.save()
    soton_sunderland = Match(home_team_obj=soton, away_team_obj=sunderland, league=l, round=r, deadline=d1); soton_sunderland.save()
    chelsea_arsenal = Match(home_team_obj=chelsea, away_team_obj=arsenal, league=l, round=r, deadline=d1); chelsea_arsenal.save()
    everton_westham = Match(home_team_obj=everton, away_team_obj=westham, league=l, round=r, deadline=d1); everton_westham.save()
    mancity_westbrom = Match(home_team_obj=mancity, away_team_obj=westbrom, league=l, round=r, deadline=d2); mancity_westbrom.save()
    liverpool_hull = Match(home_team_obj=liverpool, away_team_obj=hull, league=l, round=r, deadline=d2); liverpool_hull.save()
    tottenham_leicester = Match(home_team_obj=tottenham, away_team_obj=leicester, league=l, round=r, deadline=d3); tottenham_leicester.save()

    l = "Bundesliga"; r = "4th round"
    d1 = datetime.strptime('Sep 18 2018  3:30PM', '%b %d %Y %I:%M%p')
    d2 = datetime.strptime('Sep 18 2018  6:30PM', '%b %d %Y %I:%M%p')
    d3 = datetime.strptime('Sep 19 2018  5:30PM', '%b %d %Y %I:%M%p')
    werder_wolfsburg = Match(home_team_obj=werder, away_team_obj=wolfsburg, league=l, round=r, deadline=d1); werder_wolfsburg.save()
    bayern_schalke = Match(home_team_obj=bayern, away_team_obj=schalke, league=l, round=r, deadline=d1); bayern_schalke.save()
    dortmund_hertha = Match(home_team_obj=dortmund, away_team_obj=hertha, league=l, round=r, deadline=d1); dortmund_hertha.save()
    bayer_koln = Match(home_team_obj=bayer, away_team_obj=koln, league=l, round=r, deadline=d1); bayer_koln.save()
    darmstadt_redbull = Match(home_team_obj=darmstadt, away_team_obj=redbull, league=l, round=r, deadline=d2); darmstadt_redbull.save()
    hamburg_frankfurt = Match(home_team_obj=hamburg, away_team_obj=frankfurt, league=l, round=r, deadline=d3); hamburg_frankfurt.save()
    hoffenheim_augsburg = Match(home_team_obj=hoffenheim, away_team_obj=augsburg, league=l, round=r, deadline=d3); hoffenheim_augsburg.save()

    espanyol_barca_result = MatchEvent(match_obj=espanyol_barca, event_obj=result); espanyol_barca_result.save()
    real_eibar_result = MatchEvent(match_obj=real_eibar, event_obj=result); real_eibar_result.save()
    bilbao_villareal_result = MatchEvent(match_obj=bilbao_villareal, event_obj=result); bilbao_villareal_result.save()
    atletico_leganes_result = MatchEvent(match_obj=atletico_leganes, event_obj=result); atletico_leganes_result.save()
    granada_celta_result = MatchEvent(match_obj=granada_celta, event_obj=result); granada_celta_result.save()
    depor_valencia_result = MatchEvent(match_obj=depor_valencia, event_obj=result); depor_valencia_result.save()
    malaga_sevilla_result = MatchEvent(match_obj=malaga_sevilla, event_obj=result); malaga_sevilla_result.save()

    manutd_swansea_result = MatchEvent(match_obj=manutd_swansea, event_obj=result); manutd_swansea_result.save()
    soton_sunderland_result = MatchEvent(match_obj=soton_sunderland, event_obj=result); soton_sunderland_result.save()
    chelsea_arsenal_result = MatchEvent(match_obj=chelsea_arsenal, event_obj=result); chelsea_arsenal_result.save()
    everton_westham_result = MatchEvent(match_obj=everton_westham, event_obj=result); everton_westham_result.save()
    mancity_westbrom_result = MatchEvent(match_obj=mancity_westbrom, event_obj=result); mancity_westbrom_result.save()
    liverpool_hull_result = MatchEvent(match_obj=liverpool_hull, event_obj=result); liverpool_hull_result.save()
    tottenham_leicester_result = MatchEvent(match_obj=tottenham_leicester, event_obj=result); tottenham_leicester_result.save()

    werder_wolfsburg_result = MatchEvent(match_obj=werder_wolfsburg, event_obj=result); werder_wolfsburg_result.save()
    bayern_schalke_result = MatchEvent(match_obj=bayern_schalke, event_obj=result); bayern_schalke_result.save()
    dortmund_hertha_result = MatchEvent(match_obj=dortmund_hertha, event_obj=result); dortmund_hertha_result.save()
    bayer_koln_result = MatchEvent(match_obj=bayer_koln, event_obj=result); bayer_koln_result.save()
    darmstadt_redbull_result = MatchEvent(match_obj=darmstadt_redbull, event_obj=result); darmstadt_redbull_result.save()
    hamburg_frankfurt_result = MatchEvent(match_obj=hamburg_frankfurt, event_obj=result); hamburg_frankfurt_result.save()
    hoffenheim_augsburg_result = MatchEvent(match_obj=hoffenheim_augsburg, event_obj=result); hoffenheim_augsburg_result.save()

    espanyol_barca_halftime = MatchEvent(match_obj=espanyol_barca, event_obj=halftime); espanyol_barca_halftime.save()
    espanyol_barca_homehandy = MatchEvent(match_obj=espanyol_barca, event_obj=homehandy); espanyol_barca_homehandy.save()
    espanyol_barca_awayhandy = MatchEvent(match_obj=espanyol_barca, event_obj=awayhandy); espanyol_barca_awayhandy.save()
    espanyol_barca_goals = MatchEvent(match_obj=espanyol_barca, event_obj=goals); espanyol_barca_goals.save()
    espanyol_barca_yellows = MatchEvent(match_obj=espanyol_barca, event_obj=yellows); espanyol_barca_yellows.save()
    espanyol_barca_reds = MatchEvent(match_obj=espanyol_barca, event_obj=reds); espanyol_barca_reds.save()

    chelsea_arsenal_halftime = MatchEvent(match_obj=chelsea_arsenal, event_obj=halftime); chelsea_arsenal_halftime.save()
    chelsea_arsenal_homehandy = MatchEvent(match_obj=chelsea_arsenal, event_obj=homehandy); chelsea_arsenal_homehandy.save()
    chelsea_arsenal_awayhandy = MatchEvent(match_obj=chelsea_arsenal, event_obj=awayhandy); chelsea_arsenal_awayhandy.save()
    chelsea_arsenal_goals = MatchEvent(match_obj=chelsea_arsenal, event_obj=goals); chelsea_arsenal_goals.save()
    chelsea_arsenal_yellows = MatchEvent(match_obj=chelsea_arsenal, event_obj=yellows); chelsea_arsenal_yellows.save()
    chelsea_arsenal_reds = MatchEvent(match_obj=chelsea_arsenal, event_obj=reds); chelsea_arsenal_reds.save()

    bayern_schalke_halftime = MatchEvent(match_obj=bayern_schalke, event_obj=halftime); bayern_schalke_halftime.save()
    bayern_schalke_homehandy = MatchEvent(match_obj=bayern_schalke, event_obj=homehandy); bayern_schalke_homehandy.save()
    bayern_schalke_awayhandy = MatchEvent(match_obj=bayern_schalke, event_obj=awayhandy); bayern_schalke_awayhandy.save()
    bayern_schalke_goals = MatchEvent(match_obj=bayern_schalke, event_obj=goals); bayern_schalke_goals.save()
    bayern_schalke_yellows = MatchEvent(match_obj=bayern_schalke, event_obj=yellows); bayern_schalke_yellows.save()
    bayern_schalke_reds = MatchEvent(match_obj=bayern_schalke, event_obj=reds); bayern_schalke_reds.save()

    primera_division_3 = Collection(number=1727101, title="PD 16/17 3 matches", intro="placeholder"); primera_division_3.save()
    premier_league_3 = Collection(number=1727102, title="PL 16/17 6 matches", intro="placeholder"); premier_league_3.save()
    bundesliga_3 = Collection(number=1727103, title="PD 16/17 4 matches", intro="placeholder"); bundesliga_3.save()

    spanish_derby_3 = Collection(number=1727201, title="PD 16/17 3 derby", intro="placeholder", is_deep_analysis=True); spanish_derby_3.save()
    english_derby_3 = Collection(number=1727202, title="PD 16/17 6 derby", intro="placeholder", is_deep_analysis=True); english_derby_3.save()
    german_derby_3 = Collection(number=1727203, title="PD 16/17 4 derby", intro="placeholder", is_deep_analysis=True); german_derby_3.save()

    offer = [
        {
            'collection': primera_division_3,
            'match_events': [
                espanyol_barca_result,
                real_eibar_result,
                bilbao_villareal_result,
                atletico_leganes_result,
                granada_celta_result,
                depor_valencia_result,
                malaga_sevilla_result
            ]
        },
        {
            'collection': premier_league_3,
            'match_events': [
                manutd_swansea_result,
                soton_sunderland_result,
                chelsea_arsenal_result,
                everton_westham_result,
                mancity_westbrom_result,
                liverpool_hull_result,
                tottenham_leicester_result
            ]
        },
        {
            'collection': bundesliga_3,
            'match_events': [
                werder_wolfsburg_result,
                bayern_schalke_result,
                dortmund_hertha_result,
                bayer_koln_result,
                darmstadt_redbull_result,
                hamburg_frankfurt_result,
                hoffenheim_augsburg_result
            ]
        },
        {
            'collection': spanish_derby_3,
            'match_events': [
                espanyol_barca_result,
                espanyol_barca_halftime,
                espanyol_barca_homehandy,
                espanyol_barca_awayhandy,
                espanyol_barca_goals,
                espanyol_barca_yellows,
                espanyol_barca_reds
            ]
        },
        {
            'collection': english_derby_3,
            'match_events': [
                chelsea_arsenal_result,
                chelsea_arsenal_halftime,
                chelsea_arsenal_homehandy,
                chelsea_arsenal_awayhandy,
                chelsea_arsenal_goals,
                chelsea_arsenal_yellows,
                chelsea_arsenal_reds
            ]
        },
        {
            'collection': german_derby_3,
            'match_events': [
                bayern_schalke_result,
                bayern_schalke_halftime,
                bayern_schalke_homehandy,
                bayern_schalke_awayhandy,
                bayern_schalke_goals,
                bayern_schalke_yellows,
                bayern_schalke_reds
            ]
        }
    ]

    for data in offer:
        collection = data['collection']
        match_events = data['match_events']
        for match_event in match_events:
            MatchEventOfCollection(match_event_obj=match_event, collection_obj=collection).save()
        for boolean in [True, False]:
            for amount in [1, 10, 100]:
                RaceTicket(collection_obj=collection, bet_amount=amount, is_professional=boolean).save()

def update_week(week):
    for collection in Collection.objects.all():
        collection.status = Collection.HIDDEN
        if week == 1 and collection.number < 1725500:
            collection.status = Collection.PLAYABLE
        if week == 2 and collection.number > 1725500 and collection.number < 1726500:
            collection.status = Collection.PLAYABLE
        if week == 3 and collection.number > 1726500:
            collection.status = Collection.PLAYABLE
        collection.save()
