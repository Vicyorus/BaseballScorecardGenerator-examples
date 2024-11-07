import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SD @ BOS, 2013-07-02
# https://www.baseball-reference.com/boxes/BOS/BOS201307020.shtml
# https://www.mlb.com/gameday/padres-vs-red-sox/2013/07/02/347990/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-02 19:11-21:59",
        "at": "Fenway Park, Boston, MA",
        "att": "36,498",
        "temp": "71F, Cloudy",
        "wind": "11mph, In From RF",
        "away": {
            "team": "San Diego Padres",
            "starter": 41,
            "roster": {
                # Lineup
                11: "Logan Forsythe",
                13: "Chris Denorfia",
                18: "Carlos Quentin",
                7: "Chase Headley",
                88: "Kyle Blanks",
                15: "Jesus Guzman",
                4: "Nick Hundley",
                5: "Alexi Amarista",
                3: "Pedro Ciriaco",
                # Starting pitcher
                41: "Robbie Erlin",
                # Bench
                12: "Yasmani Grandal",
                25: "Will Venable",
                14: "Mark Kotsay",
                # Bullpen
                16: "Huston Street",
                46: "Tim Stauffer",
                55: "Dale Thayer",
                26: "Burch Smith",
                50: "Nick Vincent",
                53: "Eric Stults",
                37: "Edinson Volquez",
                38: "Tyson Ross",
                34: "Andrew Cashner",
                54: "Joe Thatcher",
                21: "Jason Marquis",
                57: "Luke Gregerson",
            },
            "lefties": [41, 53, 54],
            "lineup": [
                [11, "4"],
                [13, "9"],
                [18, "0"],
                [7, "5"],
                [88, "7"],
                [15, "3"],
                [4, "2"],
                [5, "8"],
                [3, "6"],
            ],
            "bench": [
                [12, "C"],
                [25, "RF"],
                [14, "CF"],
            ],
            "bullpen": [16, 46, 55, 26, 50, 53, 37, 38, 34, 54, 21, 57],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                23: "Brandon Snyder",
                10: "Jose Iglesias",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                37: "Mike Carp",
                76: "Jonathan Diaz",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                # Bullpen
                64: "Allen Webster",
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [39, "2"],
                [23, "5"],
                [10, "6"],
            ],
            "bench": [
                [37, "1B"],
                [76, "SS"],
                [29, "LF"],
                [20, "C"],
            ],
            "bullpen": [64, 63, 40, 30, 32, 19, 31, 36, 22, 46],
        },
        "umpires": {
            "HP": "Paul Nauert",
            "1B": "Doug Eddings",
            "2B": "Dana DeMuth",
            "3B": "Angel Hernandez",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. SD #11 Logan Forsythe (X - X - X)
t1.new_ab()
t1.pitch_list("c s c")
t1.out("!K")

# 2. SD #13 Chris Denorfia (X - X - X)
t1.new_ab()
t1.pitch_list("b s s s")
t1.out("K")

# 3. SD #18 Carlos Quentin (X - X - X)
t1.new_ab()
t1.pitch_list("s t")
t1.out("G6-3")


# Bot 1st
# Pitching: SD #41 Robbie Erlin
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b b c s")
b1.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c b f f f f")
b1.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f b b")
b1.reach("BB")
b1.advance(3, "34 2B")
b1.thrown_out(4, "34 9-4-2", 3, 41)

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("b d")
b1.hit(2)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. SD #7  Chase Headley (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("F8")

# 5. SD #88 Kyle Blanks (X - X - X)
t2.new_ab()
t2.pitch_list("s s t")
t2.out("KT")

# 6. SD #15 Jesus Guzman (X - X - X)
t2.new_ab()
t2.pitch_list("s c")
t2.hit(2)

# 7. SD #4  Nick Hundley (X - 15 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.out("F8")


# Bot 2nd
# Pitching: SD #41 Robbie Erlin
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b b f b c")
b2.out("F9")

# 6. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 5)
b2.new_ab()
b2.pitch_list("c b d s f b")
b2.out("F7")

# 8. BOS #23 Brandon Snyder (X - X - 5)
b2.new_ab()
b2.pitch_list("c c f b 1 f")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 8. SD #5  Alexi Amarista (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f f f")
t3.out("G4-3")

# 9. SD #3  Pedro Ciriaco (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(1)
t3.advance(2, "11 SB")

# 1. SD #11 Logan Forsythe (X - X - 3)
t3.new_ab()
t3.pitch_list("t 1 s s")
t3.out("K")

# 2. SD #13 Chris Denorfia (X - 3 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b")
t3.out("F7")


# Bot 3rd
# Pitching: SD #41 Robbie Erlin
b3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b c f b")
b3.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("c c b")
b3.hit(1)
b3.advance(2, "18 SB")
b3.advance(3, "18 F9")

# 2. BOS #18 Shane Victorino (X - X - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("c b")
b3.out("F9")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c b f d")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 3. SD #18 Carlos Quentin (X - X - X)
t4.new_ab()
t4.pitch_list("s b")
t4.out("F7")

# 4. SD #7  Chase Headley (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("P4")

# 5. SD #88 Kyle Blanks (X - X - X)
t4.new_ab()
t4.pitch_list("b b s")
t4.hit(2)

# 6. SD #15 Jesus Guzman (X - 88 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("f b b s b s")
t4.out("K")


# Bot 4th
# Pitching: SD #41 Robbie Erlin
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.hit(1)
b4.advance(2, "12 BB")
b4.advance(3, "39 BB")
b4.advance(4, "23 2B")

# 5. BOS #12 Mike Napoli (X - X - 34)
b4.new_ab()
b4.pitch_list("d b f b f f b")
b4.reach("BB")
b4.advance(2, "39 BB")
b4.advance(4, "23 2B")

# 6. BOS #5  Jonny Gomes (X - 34 - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("f d c b b f f s")
b4.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 34 - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("d c b b f f b")
b4.reach("BB")
b4.advance(4, "23 2B")

# 8. BOS #23 Brandon Snyder (34 - 12 - 39)
b4.new_ab(is_risp=True)
b4.pitch_list("f b s f f f b f")
b4.hit(2, rbis=3)
b4.thrown_out(3, "8-6-5", 2, 41)

# Pitching change (SD): #46 Tim Stauffer replaces #41 Robbie Erlin
b4.pitching_substitution(46)

# 9. BOS #10 Jose Iglesias (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f")
b4.hit(1)
b4.advance(2, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b4.new_ab()
b4.hit(1)

# 2. BOS #18 Shane Victorino (X - 10 - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("d d")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 7. SD #4  Nick Hundley (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)
t5.advance(3, "5 1B")

# 8. SD #5  Alexi Amarista (X - 4 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b")
t5.hit(1)
t5.thrown_out(2, "3 FC5-4", 1, 41)

# 9. SD #3  Pedro Ciriaco (4 - X - 5)
t5.new_ab(is_risp=True)
t5.reach("FC5-4")
t5.advance(2, "13 SB")

# 1. SD #11 Logan Forsythe (4 - X - 3)
t5.new_ab(is_risp=True)
t5.pitch_list("c b s f")
t5.out("(F)P3")

# 2. SD #13 Chris Denorfia (4 - X - 3)
t5.new_ab(is_risp=True)
t5.pitch_list("c s b")
t5.out("L4")


# Bot 5th
# Pitching: SD #46 Tim Stauffer
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c b f f b b f b")
b5.reach("BB")
b5.thrown_out(2, "12 CS", 3, 46)

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.pitch_list("c c d")
b5.out("F8")

# 5. BOS #12 Mike Napoli (X - X - 15)
b5.new_ab()
b5.pitch_list("b c b f b f s")
b5.out("KDP2-6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 3. SD #18 Carlos Quentin (X - X - X)
t6.new_ab()
t6.pitch_list("s b")
t6.out("G6-3")

# 4. SD #7  Chase Headley (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("G3-1")

# 5. SD #88 Kyle Blanks (X - X - X)
t6.new_ab()
t6.out("P4")


# Bot 6th
# Pitching: SD #46 Tim Stauffer
b6 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.hit(2)
b6.advance(4, "10 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 5 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b f")
b6.out("P6")

# 8. BOS #23 Brandon Snyder (X - 5 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.out("G6-3")

# 9. BOS #10 Jose Iglesias (X - 5 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("d c")
b6.hit(1, rbis=1)
b6.thrown_out(2, "8-3-6", 3, 46)


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 6. SD #15 Jesus Guzman (X - X - X)
t7.new_ab()
t7.pitch_list("f b f f b f")
t7.hit(4)

# 7. SD #4  Nick Hundley (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F8")

# 8. SD #5  Alexi Amarista (X - X - X)
t7.new_ab()
t7.pitch_list("c f f f")
t7.out("G4-3")

# 9. SD #3  Pedro Ciriaco (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("F7")


# Bot 7th
# Pitching: SD #54 Joe Thatcher
b7 = game.new_inning()

# Pitching change (SD): #54 Joe Thatcher replaces #46 Tim Stauffer
b7.pitching_substitution(54)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("c f f s")
b7.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("f f s")
b7.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")
b7.advance(2, "34 SB")

# 4. BOS #34 David Ortiz (X - X - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("c c 1 b d")
b7.out("(F)F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #41 John Lackey
t8 = game.new_inning()

# 1. SD #11 Logan Forsythe (X - X - X)
t8.new_ab()
t8.pitch_list("c b s b")
t8.out("G5-3")

# 2. SD #13 Chris Denorfia (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# 3. SD #18 Carlos Quentin (X - X - 13)
t8.new_ab()
t8.pitch_list("f b f b s")
t8.out("K")

# 4. SD #7  Chase Headley (X - X - 13)
t8.new_ab()
t8.out("F9")


# Bot 8th
# Pitching: SD #55 Dale Thayer
b8 = game.new_inning()

# Pitching change (SD): #55 Dale Thayer replaces #54 Joe Thatcher
b8.pitching_substitution(55)

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c b c b c")
b8.out("!K")

# 6. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("L8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b s b")
b8.reach("BB")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #23 Brandon Snyder, batting 8th
b8.offensive_substitution(8, 37, "PH")

# 8. BOS #37 Mike Carp (X - X - 39)
b8.new_ab()
b8.pitch_list("b b s b t f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #41 John Lackey
t9.pitching_substitution(19)

# Defensive change (BOS): #76 Jonathan Diaz replaces #37 Mike Carp (PH), playing 3B, batting 8th
t9.defensive_substitution(8, 76, "5")

# 5. SD #88 Kyle Blanks (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f f f s")
t9.out("K")

# 6. SD #15 Jesus Guzman (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("P6")

# 7. SD #4  Nick Hundley (X - X - X)
t9.new_ab()
t9.pitch_list("c s b s")
t9.out("K")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: SD
# LP: SD #41 Robbie Erlin
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
