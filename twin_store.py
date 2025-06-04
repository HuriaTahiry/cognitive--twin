import faiss
import numpy as np
import uuid
from survey_processor import build_cognitive_twin, neurotransmitter_vector


class TwinStore:
    def __init__(self, dimension=5):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = {}  
        self.id_counter = 0

    def add_twin(self, raw_input):
       
        profile = build_cognitive_twin(raw_input)
        vector = neurotransmitter_vector(profile)

      
        self.index.add(vector)

        
        twin_id = str(uuid.uuid4())
        self.metadata[self.id_counter] = {
            "uuid": twin_id,
            "profile": profile,
            "vector": vector.tolist()[0]
        }

        self.id_counter += 1
        return twin_id, vector

    def search_similar(self, query_vector, k=3):
        distances, indices = self.index.search(query_vector, k)
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx in self.metadata:
                results.append({
                    "uuid": self.metadata[idx]["uuid"],
                    "distance": float(dist),
                    "profile": self.metadata[idx]["profile"]
                })
        return results

