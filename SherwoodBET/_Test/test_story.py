from django.test import TestCase

class TestStory(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass
        # create test data
        # - teams
        # - matches
        # - events
        # - match-events
        # - collections
        # - match-events of collections
        # - race tickets

        # query database for game data

        # user authentication
        # - user login with not existing username
        # - user login with not existing email
        # - user signup with valid credentials
        # - user signup with used username
        # - user signup with used email
        # - user login with username - wrong password
        # - user login with email - wrong password
        # - user successful login

        # activate profile

        # query user profile data
        # query user account data

        # start playing
        # - get offer
        # - get one race ticket - not existing userticket
        # - getting the same ticket again (no duplicate)
        # - place bet (filling ticket)
        # - get offer again (played race tickets exist)
        # - get the filled ticket (received with the previous data)
        # - modify the ticket - place bet again
        # - play the same collection, but with other race ticket
        # - play an other collection - a deep analysis this time

        # create 45 robots

        # matches start
        # - get user tickets - all 3 modifiable
        # - get one with matches
        # - get one with deep analysis
        # - one match without additional events
        # - calculate points
        # - get user tickets again
        # - get the started one again
        # - a new match starts
        # - get it again...
        # - the matches change
        # - get it again...
        # - all matches finish

        #  wall
        # - test_user_requests_stories_without_filter
        # - test_user_requests_stories_about_announcements
        # - test_user_requests_stories_about_matches
        # - test_user_requests_stories_about_friends
        # - test_user_requests_own_stories
        # - test_user_shares_story
        # - test_user_comments_on_story
        # - test_user_likes_story

        # community
        # - test_user_searches_user_by_existing_username
        # - test_user_searches_user_by_not_existing_username
        # - test_user_searches_user_by_existing_email
        # - test_user_searches_user_by_not_existing_email
        # - test_user_sends_friend_request_for_user
        # - test_user_gets_active_friend_requests
        # - test_user_confirms_friend_request
        # - test_user_gets_preferences
        # - test_user_sets_preferences
        # - test_user_gets_questionnaires
        # - test_user_gets_questionnaire
        # - test_user_fills_questionnaire
        # - test_user_writes_opinion


    def setUp(self):
        pass

    def test_story(self):
        pass
