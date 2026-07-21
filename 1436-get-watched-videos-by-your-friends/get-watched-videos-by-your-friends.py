class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        n = len(friends)
        visited = [False] * n
        visited[id] = True

        q = deque([id])
        curr_level = 0

        # BFS until required level
        while q and curr_level < level:
            for _ in range(len(q)):
                person = q.popleft()
                for friend in friends[person]:
                    if not visited[friend]:
                        visited[friend] = True
                        q.append(friend)
            curr_level += 1

        # Count videos watched by people at target level
        freq = Counter()
        while q:
            person = q.popleft()
            for video in watchedVideos[person]:
                freq[video] += 1

        # Sort by frequency, then alphabetically
        return sorted(freq.keys(), key=lambda x: (freq[x], x))