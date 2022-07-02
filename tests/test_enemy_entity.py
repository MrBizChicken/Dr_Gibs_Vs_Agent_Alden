import unittest, sys, os, pygame

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir =os.path.dirname(currentdir)
sys.path.append(parentdir)

import enemy_entity

class Test_enemy_entity(unittest.TestCase):

    def setUp(self):
        pygame.init()
        surface = pygame.display.set_mode((100, 100))
        self.test_group = pygame.sprite.Group()
        self.test_obj = enemy_entity.Enemy_entity(0, 0, 64 ,64)

    def test_random_direction_move(self):
        pass





    def test_random_vector2(self):
        for i in range(100):
            random_direction = self.test_obj.random_vector2()
            self.assertIsInstance(random_direction, pygame.math.Vector2, "The random vector2 function didn't return a vector2. ")
            x, y = random_direction
            self.assertTrue(random_direction != pygame.math.Vector2(0, 0), f"This vector2 is not a moving vector2. This is the vector2 it has returned {random_direction}")
            self.assertFalse((y < -1 or y > 1), "This y vector2 argument is lower than -1 or higher than 1")
            self.assertFalse((x < -1 or x > 1), f"This x vector2 agrument is lower than -1 or higher than 1.  ")




if __name__ == '__main__':
    unittest.main()
