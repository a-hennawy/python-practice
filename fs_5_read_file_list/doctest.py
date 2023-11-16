def bounded_avg(nums):
    """
    returns average of a list of numbers (nums should be between 1-100)
    >>> bounded_avg([5,4,6])
    4.0
    """
    for n in nums:
        if n < 1 or n > 100:
            raise ValueError(f"{n} is not between 1-100")
        else:
            return sum(nums)//len(nums)
