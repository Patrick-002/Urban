import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return str(self.nickname)


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return str(self.current_user.nickname)

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f"Залогинился пользователь: {nickname}")
                return True
        print("Неправильное имя или пароль")
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return False
        new_user = User(nickname, password, age)
        self.current_user = new_user
        self.users.append(new_user)
        print(f"Пользователь {nickname} успешно зарегистрирован")
        return True

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            is_new = True
            for video in self.videos:
                if video == new_video:
                    is_new = False
                    break
            if is_new:
                self.videos.append(new_video)

    def get_videos(self, search_word):
        list_found_videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                list_found_videos.append(video.title)
        return list_found_videos

    def watch_video(self, video_name):
        current_video = None
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return False
        for video in self.videos:
            if video_name == video.title:
                current_video = video
                break
        if current_video is None:
            print("Видео не найдено")
            return False
        if current_video.adult_mode == True and self.current_user.age < 17:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return False
        print(f"Сейчас вы смотрите '{current_video.title}'")
        for second in range(1, current_video.duration + 1):
            print(second,  end=' ')
            current_video.time_now = second
            time.sleep(1)
        print("Конец видео")
        current_video.time_now = 0
        return True


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
