def get_rank(marks):
  data = [
      (286, 292, 19, 12),(280, 284, 42, 23),(268, 279, 106, 64),(250, 267, 524, 108),(231, 249, 1385, 546),(215, 230, 2798, 1421),(200, 214, 4667, 2863),(189, 199, 6664, 4830),(175, 188, 10746, 7152),(160, 174, 16163, 11018),(149, 159, 21145, 16495),(132, 148, 32826, 22238),(120, 131, 43174, 33636),(110, 119, 54293, 44115),(102, 109, 65758, 55269),(95, 101, 76260, 66999),(89, 94, 87219, 78111),(79, 88, 109329, 90144),(62, 87, 169542, 92303),(41, 61, 326517, 173239),(1, 40, 1025009, 334080)
  ]
  for marks_range_start, marks_range_end, rank_range_start, rank_range_end in data:
    if marks_range_start <= marks <= marks_range_end:
        return rank_range_start if marks == marks_range_start else rank_range_end

  return "NA"

# Example usage
user_marks = 208
rank = get_rank(user_marks)
print(f"The user's rank is {rank}.")
