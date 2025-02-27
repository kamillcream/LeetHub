class Solution(object):
    def videoStitching(self, clips, time):
        clips.sort(key=lambda x: (x[0], x[1]))
        if clips[0][0] > 0:
            return -1
        
        prev_start = 0
        max_end = 0
        cover = 0
        i = 0
        
        while max_end < time:
            best_end = max_end
            
            while i < len(clips) and clips[i][0] <= max_end:
                best_end = max(clips[i][1], best_end)
                i += 1
            if best_end == max_end:
                return -1
            
            max_end = best_end
            cover += 1

        return cover
    