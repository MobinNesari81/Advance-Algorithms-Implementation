def tournament_schedule(teams):
    if len(teams) == 1:
        return []

    # Divide the teams into two halves
    mid = len(teams) // 2
    first_half = teams[:mid]
    second_half = teams[mid:]

    # Recursively schedule tournaments for each half
    first_half_schedule = tournament_schedule(first_half)
    second_half_schedule = tournament_schedule(second_half)

    # Merge the schedules
    schedule = []
    for i in range(len(first_half_schedule)):
        round_i = [match + (len(second_half_schedule) + i,) for match in first_half_schedule[i]]
        schedule.append(round_i)
    for i in range(len(second_half_schedule)):
        round_i = [(match[1], match[0]) + match[2:] for match in second_half_schedule[i]]
        schedule.append(round_i)

    # Add matches between the two halves
    for i in range(mid):
        schedule.append([(first_half[i], second_half[i])])

    return schedule
