import uuid

class Tracker:
    def update(self, detections):
        tracked = []
        for det in detections:
            x1, y1, x2, y2, label = det
            tracked.append({
                "id": str(uuid.uuid4())[:8],
                "bbox": (x1, y1, x2, y2),
                "label": label
            })
        return tracked
