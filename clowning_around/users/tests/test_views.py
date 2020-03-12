import pytest
from django.conf import settings
from django.test import RequestFactory

from clowning_around.users.views import (
    UserRedirectView,
    UserUpdateView,
    ClientAppointmentListView,
    AppointmentUpdateView
)

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


class TestUserRedirectView:
    def test_get_redirect_url(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        view = UserRedirectView()
        request = request_factory.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestClientAppointmentListView:
    def test_view_appointments(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass

    def test_rate_appointment(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass


class TestTroupeLeaderView:
    def test_view_create_appointment(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass

    def test_view_assign_to_troupe(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass
    

class TestClownsView:
    def test_view_appointments(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass

    def test_view_update_appointment_status(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass

    def test_view_report_appointment_incident(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass

    def test_view_request_client_contact(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        pass