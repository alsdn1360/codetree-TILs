class agent():
    def __init__(self, code = 'A', score = 0):
        self.code = code
        self.score = score

agents = []
for _ in range(5):
    code, score = tuple(input().split())
    agents.append(agent(code, int(score)))

poor_agent = ''
min_score = 101

for i in range(5):
    if agents[i].score < min_score:
        min_score = agents[i].score
        poor_agent = agents[i].code

print(poor_agent, min_score)