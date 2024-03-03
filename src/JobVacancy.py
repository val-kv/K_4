from abc import ABC, abstractmethod

from src.hhabc import JobVacanciesAPI


class JobVacancy(JobVacanciesAPI, ABC):

    @abstractmethod
    def __init__(self, name_vacant, link_vacant, salary, currency, text, requirement, base_url):
        """
               Инициализирует класс вакансии с заданными параметрами.
               Args:
                   name_vacant (str): Название вакансии.
                   link_vacant (str): Ссылка на вакансию.
                    salary (float): Зарплата.
                   currency (str): Валюта.
                   text (str): Описание вакансии.
                   requirement (str): Требования к вакансии.
                   base_url (str): Базовый URL-адрес для API.
               Returns:
                   None
               """
        super().__init__(base_url)
        self.name_vacant = name_vacant
        self.line_vacant = link_vacant
        self.salary = salary
        self.currency = currency
        self.text = text
        self.requirements = requirement

    def __le__(self, other):
        """
        Сравните диапазон зарплат текущего объекта с другим объектом и верните значение True, если
        текущий диапазон зарплат меньше или равен диапазону зарплат другого объекта.
        Если во время сравнения возникает исключение, верните значение None.
        """
        try:
            salary_from, salary_to = self.salary.split('-')
            salary_from_other, salary_to_other = other.salary.split('-')
            if salary_to != 'None' and salary_from != 'None':
                return (int(salary_to) + int(salary_from) / 2) <= (int(salary_to_other) + int(salary_from_other) / 2)
            elif salary_to == 'None' and salary_from != 'None':
                return int(salary_from) <= int(salary_from_other)
            elif salary_to != 'None' and salary_from == 'None':
                return int(salary_to) <= int(salary_to_other)
            else:
                return int(salary_to) <= int(salary_to_other)
        except:
            return

    def __lt__(self, other):
        """
        Сравнивает зарплату self с зарплатой другого объекта.
        Возвращает значение True, если среднее значение диапазона зарплат self меньше
        среднего значения диапазона зарплат другого объекта. Возвращает значение False, если диапазон
        зарплат self выше или равен диапазону зарплат другого объекта.
        Если во время сравнения возникает исключение, None не возвращается.
        """
        try:
            salary_from, salary_to = self.salary.split('-')
            salary_from_other, salary_to_other = other.salary.split('-')
            if salary_to != 'None' and salary_from != 'None':
                return (int(salary_to) + int(salary_from) / 2) < (int(salary_to_other) + int(salary_from_other) / 2)
            elif salary_to == 'None' and salary_from != 'None':
                return int(salary_from) < int(salary_from_other)
            elif salary_to != 'None' and salary_from == 'None':
                return int(salary_to) < int(salary_to_other)
            else:
                return int(salary_to) < int(salary_to_other)
        except:
            return
