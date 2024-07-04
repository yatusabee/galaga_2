class CollisionDetector:
    def __init__(self):
        pass

    def check_collisions(self, bullets, enemies):
        for bullet in bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.handle_collision(bullet, bullets, enemy, enemies)
                    return True
        return False

    def check_collisions_powerup(self, powerups, player):
        for pu in powerups:
            if pu.rect.colliderect(player.rect):
                if pu.getTypePowerUp() == 'PowerUpBullet':
                    player.get_bullet_manager().increase_type()
                elif pu.getTypePowerUp() == 'PowerUpLife':
                    player.increase_life()
                self.handle_collision_player(pu, powerups)
                return True
        return False

    def check_collisions_player(self, bullets, player):
        '''
        método que detecta colisiones entre las minas y el jugador
        :param bullets:
        :param player:
        :return:
        '''
        for bullet in bullets:
            if bullet.rect.colliderect(player.rect):
                self.handle_collision_player(bullet, bullets)
                return True
        return False

    def handle_collision_player(self, bullet, bullets):
        '''
        Elimina de la lista de minas, a la mina que colisiono
        :param bullet:
        :param bullets:
        :return:
        '''
        if bullet in bullets:
            # si el objeto se ha eliminado de la lista, entonces no se dibuja
            bullets.remove(bullet)

    def handle_collision(self, bullet, bullets, enemy, enemies):
        if bullet in bullets:
            bullets.remove(bullet)
        if enemy in enemies:
            enemies.remove(enemy)

