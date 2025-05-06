import math

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature      # Feature index to split on
        self.threshold = threshold  # Threshold for splitting
        self.left = left            # Left child node
        self.right = right          # Right child node
        self.value = value          # Predicted class (for leaf nodes)

class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
        self.root = None
    
    def fit(self, X, y):
        self.root = self._grow_tree(X, y, depth=0)
    
    def _grow_tree(self, X, y, depth):
        n_samples = len(X)
        n_features = len(X[0]) if X else 0
        classes = list(set(y))
        
        # Stopping criteria
        if depth >= self.max_depth or len(classes) == 1 or n_samples < 2:
            return Node(value=max(set(y), key=y.count))
        
        # Find the best split
        best_gain = -1
        best_feature, best_threshold = None, None
        
        for feature in range(n_features):
            thresholds = sorted(set(row[feature] for row in X))
            for threshold in thresholds:
                left_y = [y[i] for i, row in enumerate(X) if row[feature] <= threshold]
                right_y = [y[i] for i, row in enumerate(X) if row[feature] > threshold]
                
                if not left_y or not right_y:
                    continue
                
                gain = self._information_gain(y, left_y, right_y)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold
        
        if best_gain == -1:
            return Node(value=max(set(y), key=y.count))
        
        # Split the data
        left_X, left_y = [], []
        right_X, right_y = [], []
        for i, row in enumerate(X):
            if row[best_feature] <= best_threshold:
                left_X.append(row)
                left_y.append(y[i])
            else:
                right_X.append(row)
                right_y.append(y[i])
        
        # Recursively grow left and right subtrees
        left = self._grow_tree(left_X, left_y, depth + 1)
        right = self._grow_tree(right_X, right_y, depth + 1)
        
        return Node(best_feature, best_threshold, left, right)
    
    def _information_gain(self, parent_y, left_y, right_y):
        def entropy(y):
            if not y:
                return 0
            counts = [y.count(c) for c in set(y)]
            probs = [c / len(y) for c in counts]
            return -sum(p * math.log2(p) if p > 0 else 0 for p in probs)
        
        parent_entropy = entropy(parent_y)
        n = len(parent_y)
        n_left, n_right = len(left_y), len(right_y)
        if n_left == 0 or n_right == 0:
            return 0
        
        child_entropy = (n_left / n) * entropy(left_y) + (n_right / n) * entropy(right_y)
        return parent_entropy - child_entropy
    
    def predict(self, X):
        return [self._traverse_tree(x, self.root) for x in X]
    
    def _traverse_tree(self, x, node):
        if node.value is not None:
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

# Example usage with a synthetic dataset
if __name__ == "__main__":
    # Synthetic dataset: 2 features, 2 classes
    X = [
        [2.0, 3.0], [2.5, 3.5], [3.0, 2.0], [3.5, 2.5],  # Class 0
        [5.0, 5.0], [5.5, 4.5], [4.5, 5.5], [6.0, 6.0]   # Class 1
    ]
    y = [0, 0, 0, 0, 1, 1, 1, 1]
    
    # Create and train the decision tree
    tree = DecisionTree(max_depth=3)
    tree.fit(X, y)
    
    # Predict on the same data
    predictions = tree.predict(X)
    
    # Calculate accuracy
    accuracy = sum(p == t for p, t in zip(predictions, y)) / len(y)
    
    # Print results
    print("Decision Tree Classifier (Pure Python) Results")
    print("---------------------------------------------")
    print("Dataset:")
    print("X =")
    for row in X:
        print(row)
    print("y =", y)
    print("Predictions:", predictions)
    print(f"Accuracy: {accuracy:.2f}")
    
    # Test a new sample
    test_sample = [3.0, 3.0]
    prediction = tree.predict([test_sample])[0]
    print(f"\nTest Sample: {test_sample}")
    print(f"Predicted Class: {prediction}")
