import pytest
from Utils import TryToDescribe


class TestFirstForm(TryToDescribe):

    @pytest.mark.smoke
    def test_get_link(self):
        PATH = 'file:///C:/Users/fedia/Downloads/Telegram%20Desktop' \
               '/qa-test.html'
        self.get_link(PATH)
        assert self.driver.title == 'Тест'

    @pytest.mark.parametrize(
        'login', [
            'lol..ru',
            'b123rsdffgru',
            'test@.',
            '123',
            '',
            'testprotei.ru',
            'testprotei@f.RU',
            '$%%()!@#$%^&*()_+',
            'testproteiru'
        ])
    def test_login_format_error(self, login, password='test'):

        self.first_form_testing(login, password)

        assert self.check_exists_on_login_format_error(login, password) is True

    @pytest.mark.parametrize(
        'password', [
            'asc',
            '123',
            'DSFSDFSDFFDS&',
            '$%%()!@#$%^&*()_+',
            't_1_1_43[]^%#@'
        ])
    def test_invalid_password_or_login(self, password, login='test@protei.ru'):

        self.first_form_testing(login, password)

        assert self.check_exists_on_invalid_password_or_login(
            login, password) is True

    @pytest.mark.smoke
    def test_right_login(self):

        login = 'test@protei.ru'
        password = 'test'
        self.first_form_testing(login, password)
        assert self.check_exists_on_first_form_true(login, password) is True


class TestSecondForm(TryToDescribe):
    @pytest.mark.skip
    @pytest.mark.parametrize(
        'email, tr', [
            ('lol.@s.ru', 1),
            ('didi@df.com', 2),
            ('sdf.@s.ru', 3),
            ('adf@df.com', 4),
            ('qwe@s.ru', 5),
            ('zxc@df.com', 6),
            ('jhk@s.ru', 7),
            ('tyu@df.com', 8),
            ('rty.@s.ru', 9),
            ('wert@df.com', 10),
            ('vbn@s.ru', 11),
            ('dgf@df.com', 12)
        ]
    )
    def test_data_compliance_email(self, email, tr, td=1, name='Feodor'):
        """Необходимо запускать первым тестом на второй форме"""
        self.email_and_name_on_second_for_testing(email, name)
        self.accept_data_add()
        assert self.check_data_in_table(tr, td) == email

    @pytest.mark.parametrize(
        'email, name', [
            ('lalala@maru', 'фыв'),
            ('123@lf.r', '123'),
            ('la21ma@.ru', 'Abcdef'),
            ('badam@.ru', ' ')
        ]
    )
    def test_email_and_name(self, email, name):
        self.email_and_name_on_second_for_testing(email, name)

        assert self.check_exits_on_data_add() is True

    def test_name_error(self, email='qwwq@na.com', name=''):
        self.email_and_name_on_second_for_testing(email, name)
        assert self.check_name_error() is True

    @pytest.mark.parametrize(
        'male', [
            'Мужской',
            'Женский'
        ]
    )
    def test_male(self, male, email='test@na.com', name='test_name'):
        self.select_male(male)
        self.email_and_name_on_second_for_testing(email, name)
        self.accept_data_add()

    @pytest.mark.parametrize(
        'choice', [
            '1',
            '2',
            '1',
            '2'
        ]
    )
    def test_check_box(self, choice, email='test@na.com', name='test_name'):

        self.select_var_1(choice)
        self.email_and_name_on_second_for_testing(email, name)
        self.accept_data_add()

    @pytest.mark.parametrize(
        'numb', [
            '1',
            '2',
            '3',
            '1'
        ]
    )
    def test_radio_button(self, numb, email='test@na.com', name='test_name'):
        self.select_var_2(numb)
        self.email_and_name_on_second_for_testing(email, name)
        self.accept_data_add()

    @pytest.mark.parametrize(
        'email', [
            '123',
            'la21maru',
            '',
            '1@.',
        ]
    )
    def test_email_format_error(self, email, name='test'):

        self.email_and_name_on_second_for_testing(email, name)
        assert self.email_format_testing(email, name) is True
