import sys
sys.path.append('../')
from utils import get_center_of_bbox, measure_distance

class PlayerBallAssigner:
  def __init__(self):
    self.max_player_ball_distance = 60
    
  def assign_ball_to_player(self, players, ball_bbox):
    ball_position = get_center_of_bbox(ball_bbox)

    closest_player = None
    min_distance = float('inf')
    
    for player_id, player in players.items():
      bbox = player['bbox']
        
      left_distance = measure_distance((bbox[0], bbox[-1]), ball_position)
      right_distance = measure_distance((bbox[2], bbox[-1]), ball_position)
      distance = min(left_distance, right_distance)
        
      if distance < self.max_player_ball_distance and distance < min_distance:
        min_distance = distance
        closest_player = player_id
    
    return closest_player
  
  