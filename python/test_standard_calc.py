from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_positive_within_range():
    """Test angles already within [-180, 180)"""
    assert bound_to_180(135) == 135
    assert bound_to_180(90) == 90
    assert bound_to_180(45) == 45
    assert bound_to_180(179) == 179


def test_bound_negative_within_range():
    """Test negative angles within range"""
    assert bound_to_180(-90) == -90
    assert bound_to_180(-135) == -135
    assert bound_to_180(-179) == -179


def test_bound_positive_outside_range():
    """Test positive angles that need to be bounded"""
    assert bound_to_180(200) == -160  # As given in example
    assert bound_to_180(180) == -180  # Boundary case
    assert bound_to_180(270) == -90
    assert bound_to_180(360) == 0
    assert bound_to_180(450) == 90  # 450 - 360 = 90


def test_bound_negative_outside_range():
    """Test negative angles that need to be bounded"""
    assert bound_to_180(-200) == 160  # -200 + 360 = 160
    assert bound_to_180(-270) == 90   # -270 + 360 = 90
    assert bound_to_180(-360) == 0    # -360 + 360 = 0
    assert bound_to_180(-450) == -90  # -450 + 720 = 270, then 270 - 360 = -90


def test_bound_large_angles():
    """Test very large positive and negative angles"""
    assert bound_to_180(720) == 0     # 720 % 360 = 0
    assert bound_to_180(1080) == 0    # 1080 % 360 = 0
    assert bound_to_180(-720) == 0    # -720 % 360 = 0


def test_bound_edge_cases():
    """Test edge cases for bound_to_180"""
    assert bound_to_180(180) == -180    # Exactly 180 becomes -180
    assert bound_to_180(-180) == -180   # -180 stays -180
    assert bound_to_180(179.99) == 179.99  # Just under 180
    assert bound_to_180(-179.99) == -179.99  # Just over -180


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_examples_from_docstring():
    """Test the examples given in the function docstring"""
    assert is_angle_between(0, 45, 90) is True
    assert is_angle_between(45, 90, 270) is False


def test_between_simple_cases():
    """Test simple cases where angles are clearly between"""
    assert is_angle_between(0, 30, 60) is True
    assert is_angle_between(10, 20, 30) is True
    assert is_angle_between(-30, 0, 30) is True


def test_between_boundary_cases():
    """Test boundary cases"""
    assert is_angle_between(0, 0, 90) is True   # Middle equals first
    assert is_angle_between(0, 90, 90) is True  # Middle equals second
    assert is_angle_between(0, 45, 90) is True  # Middle is between


def test_between_reflex_angles():
    """Test cases involving reflex angles (> 180 degrees span)"""
    # When first and second span more than 180 degrees, middle should NOT be in that span
    assert is_angle_between(45, 90, 270) is False  # 90 is in the reflex portion
    assert is_angle_between(270, 0, 45) is True    # 0 is NOT in the reflex portion
    assert is_angle_between(270, 180, 45) is False  # 180 is in the reflex portion


def test_between_crossing_180():
    """Test cases that cross the -180/+180 boundary"""
    assert is_angle_between(170, 180, -170) is True  # 180 is between 170 and -170
    assert is_angle_between(170, -180, -170) is True  # -180 is between 170 and -170
    assert is_angle_between(-170, 0, 170) is False   # 0 is in reflex angle


def test_between_same_angles():
    """Test edge cases where angles are the same"""
    assert is_angle_between(45, 45, 45) is True  # All same
    assert is_angle_between(0, 180, 0) is True   # First and second same, spanning 180


def test_between_normalized_input():
    """Test that function works with angles outside [-180, 180)"""
    assert is_angle_between(360, 405, 450) is True  # Same as (0, 45, 90)
    assert is_angle_between(-360, -315, -270) is True  # Same as (0, 45, 90)


def test_between_zero_degree_spans():
    """Test cases where the angular span is zero"""
    assert is_angle_between(90, 90, 90) is True    # All angles identical
    assert is_angle_between(0, 0, 0) is True       # All zero
    assert is_angle_between(-90, -90, -90) is True  # All negative identical


def test_between_exact_180_spans():
    """Test cases with exactly 180 degree spans"""
    assert is_angle_between(0, 180, 180) is True   # Middle at end of 180° span
    assert is_angle_between(0, -180, 180) is True  # Middle at start of 180° span
    assert is_angle_between(90, -90, 270) is True  # 180° span, middle at opposite
    assert is_angle_between(45, -135, 225) is True  # 180° span different orientation


def test_between_very_close_angles():
    """Test cases with very small angular differences"""
    assert is_angle_between(0, 0.1, 0.2) is True    # Tiny clockwise arc
    assert is_angle_between(0, -0.1, -0.2) is True  # Tiny counter-clockwise arc
    assert is_angle_between(179, 179.5, -179) is True  # Small arc crossing boundary


def test_between_almost_reflex():
    """Test cases just at the reflex angle boundary"""
    assert is_angle_between(0, 90, 179) is True     # Just under 180°, should be normal
    assert is_angle_between(0, 90, 181) is False    # Just over 180°, should be reflex
    assert is_angle_between(0, -90, -179) is True   # Just under 180° counter-clockwise
    assert is_angle_between(0, -90, -181) is False  # Just over 180° counter-clockwise


def test_between_multiple_rotations():
    """Test with angles requiring multiple full rotations"""
    assert is_angle_between(720, 765, 810) is True  # Same as (0, 45, 90)
    assert is_angle_between(-720, -675, -630) is True  # Multiple negative rotations
    assert is_angle_between(1080, 45, 1170) is True  # Mixed large and normal angles


def test_bound_fractional_angles():
    """Test bound_to_180 with fractional angles"""
    assert bound_to_180(359.5) == -0.5
    assert bound_to_180(180.5) == -179.5
    assert bound_to_180(-180.5) == 179.5
    assert bound_to_180(0.5) == 0.5
