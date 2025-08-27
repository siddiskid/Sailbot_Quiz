def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    # Wrap to [0, 360) first
    angle = angle % 360

    # Then shift to [-180, 180)
    if angle >= 180:
        angle -= 360

    return angle


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    # Get shortest angular distances
    diff_first_to_second = bound_to_180(second_angle - first_angle)
    diff_first_to_middle = bound_to_180(middle_angle - first_angle)

    # Edge case: same start/end angle
    if abs(diff_first_to_second) == 0:
        return True

    # Edge case: exactly opposite angles
    if abs(diff_first_to_second) == 180:
        return abs(diff_first_to_middle) == 180

    # Normal case: arc < 180 degrees
    if abs(diff_first_to_second) < 180:
        if diff_first_to_second > 0:
            # Clockwise arc
            return 0 <= diff_first_to_middle <= diff_first_to_second
        else:
            # Counter-clockwise arc
            return diff_first_to_second <= diff_first_to_middle <= 0

    # Reflex angle: arc > 180 degrees
    # Check if middle is NOT in the shorter arc
    else:
        if diff_first_to_second > 0:
            return not (diff_first_to_middle < 0 and diff_first_to_middle > diff_first_to_second - 360)
        else:
            return not (diff_first_to_middle > 0 and diff_first_to_middle < diff_first_to_second + 360)
