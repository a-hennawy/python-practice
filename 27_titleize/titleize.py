def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    caps = ""
    for i in phrase.split(" "):
        caps += " " + i.capitalize()
    return caps.strip()
