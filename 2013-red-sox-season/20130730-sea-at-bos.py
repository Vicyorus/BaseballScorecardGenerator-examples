import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SEA @ BOS, 2013-07-30
# https://www.baseball-reference.com/boxes/BOS/BOS201307300.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2013/07/30/348335/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-30 19:12-21:56",
        "at": "Fenway Park, Boston, MA",
        "att": "34,578",
        "temp": "78F, Cloudy",
        "wind": "2mph, In From LF",
        "away": {
            "team": "Seattle Mariners",
            "starter": 23,
            "roster": {
                # Lineup
                5: "Brad Miller",
                6: "Nick Franklin",
                15: "Kyle Seager",
                8: "Kendrys Morales",
                28: "Raul Ibanez",
                38: "Michael Morse",
                17: "Justin Smoak",
                55: "Michael Saunders",
                33: "Henry Blanco",
                # Starting pitcher
                23: "Joe Saunders",
                # Bench
                26: "Brendan Ryan",
                9: "Endy Chavez",
                13: "Dustin Ackley",
                35: "Humberto Quintero",
                # Bullpen
                44: "Lucas Luetge",
                39: "Aaron Harang",
                50: "Erasmo Ramírez",
                40: "Danny Farquhar",
                37: "Brandon Maurer",
                41: "Charlie Furbush",
                59: "Oliver Pérez",
                31: "Yoervis Medina",
                34: "Félix Hernández",
                54: "Tom Wilhelmsen",
                18: "Hisashi Iwakuma",
            },
            "lefties": [23, 44, 41, 59],
            "lineup": [
                [5, "6"],
                [6, "4"],
                [15, "5"],
                [8, "0"],
                [28, "7"],
                [38, "9"],
                [17, "3"],
                [55, "8"],
                [33, "2"],
            ],
            "bench": [
                [26, "SS"],
                [9, "CF"],
                [13, "2B"],
                [35, "C"],
            ],
            "bullpen": [44, 39, 50, 40, 37, 41, 59, 31, 34, 54, 18],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 67,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                67: "Brandon Workman",
                # Bench
                37: "Mike Carp",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                65: "Jose De La Torre",
                41: "John Lackey",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [5, "7"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [37, "1B"],
                [29, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 41, 32, 66, 31, 36, 19, 38, 54, 22, 46],
        },
        "umpires": {
            "HP": "Chris Conroy",
            "1B": "Gary Darling",
            "2B": "David Rackley",
            "3B": "Jerry Meals",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #67 Brandon Workman
t1 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G4-3")

# 2. SEA #6  Nick Franklin (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.hit(2)
t1.advance(3, "15 F8")
t1.advance(4, "8 1B")

# 3. SEA #15 Kyle Seager (X - 6 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b b c f")
t1.out("F8")

# 4. SEA #8  Kendrys Morales (6 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b b s b f")
t1.hit(1, rbis=1)

# 5. SEA #28 Raul Ibanez (X - X - 8)
t1.new_ab()
t1.pitch_list("c s s")
t1.out("K")


# Bot 1st
# Pitching: SEA #23 Joe Saunders
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("f b f s")
b1.out("K2-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b")
b1.hit(2)
b1.advance(3, "15 E6")
b1.advance(4, "34 PB")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.error(6)
b1.reach("E6")
b1.advance(2, "34 PB")
b1.advance("U", "34 1B")

# 4. BOS #34 David Ortiz (18 - X - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b b c s")
b1.pb()
b1.hit(1, rbis=1)
b1.advance(2, "39 1B")
b1.advance(3, "5 BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
b1.new_ab()
b1.pitch_list("b d c s s")
b1.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 34)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(2, "5 BB")

# 7. BOS #5  Jonny Gomes (X - 34 - 39)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b d b")
b1.reach("BB")

# 8. BOS #7  Stephen Drew (34 - 39 - 5)
b1.new_ab(is_risp=True)
b1.out("G3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #67 Brandon Workman
t2 = game.new_inning()

# 6. SEA #38 Michael Morse (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b s")
t2.out("K")

# 7. SEA #17 Justin Smoak (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F7")

# 8. SEA #55 Michael Saunders (X - X - X)
t2.new_ab()
t2.pitch_list("f b b b f b")
t2.reach("BB")

# 9. SEA #33 Henry Blanco (X - X - 55)
t2.new_ab()
t2.pitch_list("c 1 s b s")
t2.out("K")


# Bot 2nd
# Pitching: SEA #23 Joe Saunders
b2 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.hit(1)
b2.thrown_out(2, "7-4-3-6", 1, 23)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.hit(4)

# 2. BOS #18 Shane Victorino (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b c f")
b2.hit(1)
b2.advance(4, "15 HR")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b2.new_ab()
b2.pitch_list("b f f 1 b f b f f")
b2.hit(4, rbis=2)

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("f f s")
b2.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b b f s c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #67 Brandon Workman
t3 = game.new_inning()

# 1. SEA #5  Brad Miller (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F8")

# 2. SEA #6  Nick Franklin (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b f s")
t3.out("K")

# 3. SEA #15 Kyle Seager (X - X - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.hit(1)

# 4. SEA #8  Kendrys Morales (X - X - 15)
t3.new_ab()
t3.pitch_list("c f")
t3.out("F9")


# Bot 3rd
# Pitching: SEA #23 Joe Saunders
b3 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.out("G5-3")

# 7. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G3")

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("c c b b b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #67 Brandon Workman
t4 = game.new_inning()

# 5. SEA #28 Raul Ibanez (X - X - X)
t4.new_ab()
t4.pitch_list("c s c")
t4.out("!K")

# 6. SEA #38 Michael Morse (X - X - X)
t4.new_ab()
t4.pitch_list("f s s")
t4.out("K")

# 7. SEA #17 Justin Smoak (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("L6")


# Bot 4th
# Pitching: SEA #23 Joe Saunders
b4 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b4.new_ab()
b4.pitch_list("l b b c")
b4.out("L4")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.pitch_list("s c b b")
b4.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b c f f b b")
b4.hit(2)
b4.advance(4, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.hit(1, rbis=1)
b4.thrown_out(2, "8-4-3", 3, 23)


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #67 Brandon Workman
t5 = game.new_inning()

# 8. SEA #55 Michael Saunders (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F9")

# 9. SEA #33 Henry Blanco (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("P4")

# 1. SEA #5  Brad Miller (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b")
t5.out("F7")


# Bot 5th
# Pitching: SEA #23 Joe Saunders
b5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.out("G3")

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("f b b f b f")
b5.out("L4")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #67 Brandon Workman
t6 = game.new_inning()

# 2. SEA #6  Nick Franklin (X - X - X)
t6.new_ab()
t6.pitch_list("c f b s")
t6.out("K")

# 3. SEA #15 Kyle Seager (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(1)
t6.advance(2, "8 1B")
t6.advance(3, "28 1B")

# 4. SEA #8  Kendrys Morales (X - X - 15)
t6.new_ab()
t6.pitch_list("c b b f")
t6.hit(1)
t6.advance(2, "28 1B")

# 5. SEA #28 Raul Ibanez (X - 15 - 8)
t6.new_ab(is_risp=True)
t6.pitch_list("f b f f d f")
t6.hit(1)

# 6. SEA #38 Michael Morse (15 - 8 - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("c s f d f s")
t6.out("K")

# 7. SEA #17 Justin Smoak (15 - 8 - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("c b f b f s")
t6.out("K")


# Bot 6th
# Pitching: SEA #37 Brandon Maurer
b6 = game.new_inning()

# Pitching change (SEA): #37 Brandon Maurer replaces #23 Joe Saunders
b6.pitching_substitution(37)

# 7. BOS #5  Jonny Gomes (X - X - X)
b6.new_ab()
b6.pitch_list("c b c")
b6.out("G5-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("b c s")
b6.out("G6-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("s c b")
b6.out("G1-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Craig Breslow
t7 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #67 Brandon Workman
t7.pitching_substitution(32)

# 8. SEA #55 Michael Saunders (X - X - X)
t7.new_ab()
t7.pitch_list("b b f b f f")
t7.out("G3")

# 9. SEA #33 Henry Blanco (X - X - X)
t7.new_ab()
t7.pitch_list("b c f")
t7.out("(F)P5")

# 1. SEA #5  Brad Miller (X - X - X)
t7.new_ab()
t7.out("G6-3")


# Bot 7th
# Pitching: SEA #37 Brandon Maurer
b7 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G3-1")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #38 Matt Thornton
t8 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #32 Craig Breslow
t8.pitching_substitution(38)

# 2. SEA #6  Nick Franklin (X - X - X)
t8.new_ab()
t8.out("F9")

# 3. SEA #15 Kyle Seager (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b c")
t8.out("!K")

# 4. SEA #8  Kendrys Morales (X - X - X)
t8.new_ab()
t8.pitch_list("f s f b f s")
t8.out("K")


# Bot 8th
# Pitching: SEA #37 Brandon Maurer
b8 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b b b")
b8.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.hit(1)
b8.advance(4, "39 HR")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b8.new_ab()
b8.pitch_list("b s b b")
b8.hit(4, rbis=2)

# 7. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c s c")
b8.out("!K")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #54 Pedro Beato
t9 = game.new_inning()

# Pitching change (BOS): #54 Pedro Beato replaces #38 Matt Thornton
t9.pitching_substitution(54)

# Defensive change (BOS): #23 Brandon Snyder replaces #10 Jose Iglesias (3B), playing 3B, batting 9th
t9.defensive_substitution(9, 23, "5")

# 5. SEA #28 Raul Ibanez (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("L9")

# 6. SEA #38 Michael Morse (X - X - X)
t9.new_ab()
t9.pitch_list("b c f f f")
t9.out("G5-3")

# 7. SEA #17 Justin Smoak (X - X - X)
t9.new_ab()
t9.pitch_list("b b f s b")
t9.hit(1)
t9.advance(2, "55 BB")
t9.advance(4, "33 1B")

# 8. SEA #55 Michael Saunders (X - X - 17)
t9.new_ab()
t9.pitch_list("b b s b b")
t9.reach("BB")
t9.advance(3, "33 1B")

# 9. SEA #33 Henry Blanco (X - 17 - 55)
t9.new_ab(is_risp=True)
t9.pitch_list("f b")
t9.hit(1, rbis=1)

# 1. SEA #5  Brad Miller (55 - X - 33)
t9.new_ab(is_risp=True)
t9.pitch_list("s s c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #67 Brandon Workman
game.winning_pitcher(67)

# Loser team: SEA
# LP: SEA #23 Joe Saunders
game.losing_pitcher(23, is_away_team=True)

# print(game)
game.generate_scorecard()
