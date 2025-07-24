import random
from collections import deque
from typing import List, Tuple

class Maze:
    def __init__(self, width: int = 6, height: int = 6, obstacle_ratio: float = 0.2):
        self.width = width
        self.height = height
        self.start = (0, 0)
        self.goal = (width - 1, height - 1)
        self.obstacles = self._generate_obstacles(obstacle_ratio)

    def _generate_obstacles(self, ratio: float) -> List[Tuple[int, int]]:
        obstacles = []
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) not in [self.start, self.goal] and random.random() < ratio:
                    obstacles.append((x, y))
        return obstacles

    def is_free(self, pos: Tuple[int, int]) -> bool:
        x, y = pos
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        return pos not in self.obstacles

class RuleSolver:
    """Breadth-first search for a path."""
    def __init__(self, maze: Maze):
        self.maze = maze

    def solve(self) -> List[Tuple[int, int]]:
        start, goal = self.maze.start, self.maze.goal
        queue = deque([(start, [start])])
        visited = {start}
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == goal:
                return path
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                new_pos = (nx, ny)
                if new_pos not in visited and self.maze.is_free(new_pos):
                    visited.add(new_pos)
                    queue.append((new_pos, path + [new_pos]))
        return []

class QLearningAgent:
    def __init__(self, maze: Maze, episodes: int = 500, alpha: float = 0.1, gamma: float = 0.9, epsilon: float = 0.2):
        self.maze = maze
        self.q = {
            (x, y): [0, 0, 0, 0] for x in range(maze.width) for y in range(maze.height)
        }
        self.episodes = episodes
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = [(-1,0),(1,0),(0,-1),(0,1)]

    def _choose_action(self, state: Tuple[int, int]) -> int:
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        q_values = self.q[state]
        return q_values.index(max(q_values))

    def _step(self, state: Tuple[int, int], action_idx: int) -> Tuple[Tuple[int, int], float, bool]:
        dx, dy = self.actions[action_idx]
        new_state = (state[0] + dx, state[1] + dy)
        if not self.maze.is_free(new_state):
            reward = -1
            new_state = state
            done = False
        elif new_state == self.maze.goal:
            reward = 10
            done = True
        else:
            reward = -0.1
            done = False
        return new_state, reward, done

    def train(self):
        for _ in range(self.episodes):
            state = self.maze.start
            done = False
            while not done:
                action = self._choose_action(state)
                next_state, reward, done = self._step(state, action)
                best_next = max(self.q[next_state])
                self.q[state][action] += self.alpha * (reward + self.gamma * best_next - self.q[state][action])
                state = next_state

    def run(self) -> List[Tuple[int, int]]:
        state = self.maze.start
        path = [state]
        steps = 0
        while state != self.maze.goal and steps < 100:
            action = self._choose_action(state)
            next_state, _, _ = self._step(state, action)
            if next_state == state:
                break
            path.append(next_state)
            state = next_state
            steps += 1
        return path

if __name__ == "__main__":
    random.seed(42)
    maze = Maze(width=6, height=6, obstacle_ratio=0.2)
    print("Maze obstacles:", maze.obstacles)

    rule_solver = RuleSolver(maze)
    rule_path = rule_solver.solve()
    print("\nChemin trouvé par règle:")
    print(rule_path)

    agent = QLearningAgent(maze)
    agent.train()
    ai_path = agent.run()
    print("\nChemin trouvé par apprentissage:")
    print(ai_path)
