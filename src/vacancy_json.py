import json
from abc import ABC, abstractmethod


class VacancyFileStorage(ABC):
    @abstractmethod
    def add_vacancy_to_file(self, vacancy):
        """
        Добавляет новую вакансию в файл.
        Args:
            self: экземпляр класса.
            vacancy: Объект вакансии.
        Returns:
            None
        """
        with open('vacancies.json', 'w') as file:
            data = json.load(file)
            data['vacancies'].append({
                'title': vacancy.title,
                'link': vacancy.link,
                'salary': vacancy.salary,
                'currency': vacancy.currency,
                'text': vacancy.text,
                'requirements': vacancy.requirements
            })
            file.seek(0)
            json.dump(data, file, indent=4)

    @abstractmethod
    def get_vacancies_from_file(self, criteria):
        """
        Извлекает и возвращает список вакансий из файла на основе заданных критериев.
        :param criteria: dict - словарь с критериями.
        :return: list - список вакансий.
        """
        with open('vacancies.json', 'r') as file:
            data = json.load(file)
            return data

    def remove_vacancy_from_file(self, vacancy):
        """
        удаляет вакансию из файла.

        :param vacancy: вакансия для удаления
        :return: None
        """
        with open('vacancies.json', 'r+') as file:
            data = json.load(file)
            data['vacancies'] = [v for v in data['vacancies'] if v['title'] != vacancy.title]
            file.seek(0)
            json.dump(data, file, indent=4)


class JSONFileStorage(VacancyFileStorage):
    def add_vacancy_to_file(self, vacancy):
        """
        добавляет новую вакансию в файл.
        Parameters:
            self (obj): экземпляр класса.
            vacancy (obj): объект вакансии.
        Returns:
            None
        """
        with open('vacancies.json', 'r+') as file:
            data = json.load(file)
            data['vacancies'].append({
                'title': vacancy.title,
                'link': vacancy.link,
                'salary': vacancy.salary,
                'description': vacancy.description
            })
            file.seek(0)
            json.dump(data, file, indent=4)

    def get_vacancies_from_file(self, criteria):
        """
        читает данные из 'vacancies.json' файла и добавляет их в список вакансий.
        Args:
            criteria: критерии поиска вакансий.
        Returns:
            данные из 'vacancies.json' файла.
        """
        with open('vacancies.json', 'r') as file:
            data = json.load(file)
            return data

    def remove_vacancy_from_file(self, vacancy):
        """
        Удаляет конкретную вакансию из списка 'vacancies.json' файла.
        Args:
        self: Экземпляр класса.
        vacancy: Объект вакансии, подлежащий удалению из файла.
        Returns:
            None
        """
        with open('vacancies.json', 'r+') as file:
            data = json.load(file)
            data['vacancies'] = [v for v in data['vacancies'] if v['title'] != vacancy.title]
            file.seek(0)
            json.dump(data, file, indent=4)
