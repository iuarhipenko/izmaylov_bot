import _sqlite3

class SQLighter:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор совединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cusor()

    def get_subscription(self, status = True):
        """Получаем всех активных клиентво бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ? ", (status,)).fetchall()

    def subscriber_exist(self, user_id):
        """Проверяем есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ? ", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True):
      """Добавлем нового подписчика"""
      with self.connection:
          result = self.cursor.execute("INSERT INTO `subscriptions` (`user_id, status`) VALUES (?,?)", (user_id, status)).fetchall()
          return bool(len(result))

    def update_subscription(self, user_id, status):
      """Обновляем статус подписки"""
      with self.connection:
          result = self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = >?", (status, user_id)).fetchall()
          return bool(len(result))

    def close(self):
      """Обновляем статус подписки"""
      return self.connection.close()
