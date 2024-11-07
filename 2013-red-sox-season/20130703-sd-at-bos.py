import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SD @ BOS, 2013-07-03
# https://www.baseball-reference.com/boxes/BOS/BOS201307030.shtml
# https://www.mlb.com/gameday/padres-vs-red-sox/2013/07/03/348005/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-03 19:12-22:17",
        "at": "Fenway Park, Boston, MA",
        "att": "36,911",
        "temp": "87F, Cloudy",
        "wind": "18mph, Out To CF",
        "away": {
            "team": "San Diego Padres",
            "starter": 37,
            "roster": {
                # Lineup
                11: "Logan Forsythe",
                13: "Chris Denorfia",
                18: "Carlos Quentin",
                7: "Chase Headley",
                88: "Kyle Blanks",
                15: "Jesus Guzman",
                12: "Yasmani Grandal",
                3: "Pedro Ciriaco",
                5: "Alexi Amarista",
                # Starting pitcher
                37: "Edinson Volquez",
                # Bench
                4: "Nick Hundley",
                25: "Will Venable",
                14: "Mark Kotsay",
                # Bullpen
                16: "Huston Street",
                46: "Tim Stauffer",
                55: "Dale Thayer",
                41: "Robbie Erlin",
                26: "Burch Smith",
                50: "Nick Vincent",
                53: "Eric Stults",
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
                [18, "7"],
                [7, "5"],
                [88, "0"],
                [15, "3"],
                [12, "2"],
                [3, "6"],
                [5, "8"],
            ],
            "bench": [
                [4, "C"],
                [25, "RF"],
                [14, "CF"],
            ],
            "bullpen": [16, 46, 55, 41, 26, 50, 53, 38, 34, 54, 21, 57],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                23: "Brandon Snyder",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                76: "Jonathan Diaz",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                5: "Jonny Gomes",
                # Bullpen
                64: "Allen Webster",
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [37, "3"],
                [39, "2"],
                [23, "5"],
                [10, "6"],
            ],
            "bench": [
                [76, "SS"],
                [12, "1B"],
                [20, "C"],
                [5, "LF"],
            ],
            "bullpen": [64, 63, 40, 41, 30, 32, 19, 36, 22, 46],
        },
        "umpires": {
            "HP": "Doug Eddings",
            "1B": "Dana DeMuth",
            "2B": "Angel Hernandez",
            "3B": "Paul Nauert",
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
# Pitching: BOS #31 Jon Lester
t1 = game.new_inning()

# 1. SD #11 Logan Forsythe (X - X - X)
t1.new_ab()
t1.pitch_list("b f c b")
t1.out("F8")

# 2. SD #13 Chris Denorfia (X - X - X)
t1.new_ab()
t1.pitch_list("c c f f b f b s")
t1.out("K")

# 3. SD #18 Carlos Quentin (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(3, "7 1B")
t1.advance(4, "88 1B")

# 4. SD #7  Chase Headley (X - X - 18)
t1.new_ab()
t1.pitch_list("s d s b f f f f f")
t1.hit(1)
t1.advance(2, "88 1B")

# 5. SD #88 Kyle Blanks (18 - X - 7)
t1.new_ab(is_risp=True)
t1.hit(1, rbis=1)

# 6. SD #15 Jesus Guzman (X - 7 - 88)
t1.new_ab(is_risp=True)
t1.pitch_list("c d s b f")
t1.out("L3")


# Bot 1st
# Pitching: SD #37 Edinson Volquez
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c f")
b1.out("G3-1")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c b")
b1.hit(2)
b1.advance(3, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c f")
b1.hit(1)
b1.advance(2, "34 SB")
b1.thrown_out(2, "34 DP6", 3, 37)

# 4. BOS #34 David Ortiz (18 - X - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b b c f b")
b1.out("DP6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 7. SD #12 Yasmani Grandal (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.out("G1-6-3")

# 8. SD #3  Pedro Ciriaco (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("(F)P3")

# 9. SD #5  Alexi Amarista (X - X - X)
t2.new_ab()
t2.out("L4")


# Bot 2nd
# Pitching: SD #37 Edinson Volquez
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c c b b")
b2.hit(1)

# 6. BOS #37 Mike Carp (X - X - 29)
b2.new_ab()
b2.pitch_list("b f s c")
b2.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b2.new_ab()
b2.pitch_list("c d f b b s")
b2.out("K")

# 8. BOS #23 Brandon Snyder (X - X - 29)
b2.new_ab()
b2.pitch_list("c d f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 1. SD #11 Logan Forsythe (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b")
t3.out("G6-3")

# 2. SD #13 Chris Denorfia (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("L8")

# 3. SD #18 Carlos Quentin (X - X - X)
t3.new_ab()
t3.pitch_list("s s b")
t3.hit(2)

# 4. SD #7  Chase Headley (X - 18 - X)
t3.new_ab(is_risp=True)
t3.out("G5-3")


# Bot 3rd
# Pitching: SD #37 Edinson Volquez
b3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.reach("HBP")
b3.advance(2, "2 1B")
b3.advance(3, "18 G1-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(1)
b3.advance(2, "18 G1-3")

# 2. BOS #18 Shane Victorino (X - 10 - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("c b c f")
b3.out("G1-3")

# 3. BOS #15 Dustin Pedroia (10 - 2 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b b s f c")
b3.out("!K")

# 4. BOS #34 David Ortiz (10 - 2 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("i i i i")
b3.reach("IBB")

# 5. BOS #29 Daniel Nava (10 - 2 - 34)
b3.new_ab(is_risp=True)
b3.pitch_list("c c d b")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 5. SD #88 Kyle Blanks (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("L8")

# 6. SD #15 Jesus Guzman (X - X - X)
t4.new_ab()
t4.pitch_list("s f b b b s")
t4.out("K")

# 7. SD #12 Yasmani Grandal (X - X - X)
t4.new_ab()
t4.hit(2)

# 8. SD #3  Pedro Ciriaco (X - 12 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("d s b f b f")
t4.out("G4-3")


# Bot 4th
# Pitching: SD #37 Edinson Volquez
b4 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(4, "39 2B")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b4.new_ab()
b4.pitch_list("f b")
b4.hit(2, rbis=1)

# 8. BOS #23 Brandon Snyder (X - 39 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("f b")
b4.out("G5-3")

# 9. BOS #10 Jose Iglesias (X - 39 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b c s b")
b4.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b c")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 9. SD #5  Alexi Amarista (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G4-3")

# 1. SD #11 Logan Forsythe (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c")
t5.out("G5-3")

# 2. SD #13 Chris Denorfia (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G5-3")


# Bot 5th
# Pitching: SD #37 Edinson Volquez
b5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("b c b")
b5.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b s c b")
b5.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("L7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 3. SD #18 Carlos Quentin (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "7 BB")
t6.advance(3, "88 DP4-6-3")

# 4. SD #7  Chase Headley (X - X - 18)
t6.new_ab()
t6.pitch_list("b b c b f b")
t6.reach("BB")
t6.thrown_out(2, "88 DP4-6-3", 1, 31)

# 5. SD #88 Kyle Blanks (X - 18 - 7)
t6.new_ab(is_risp=True)
t6.pitch_list("b f")
t6.out("DP4-6-3")

# 6. SD #15 Jesus Guzman (18 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c f s")
t6.out("K")


# Bot 6th
# Pitching: SD #37 Edinson Volquez
b6 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("F8")

# 6. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.hit(2)

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f f s")
b6.out("K")

# 8. BOS #23 Brandon Snyder (X - 37 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 7. SD #12 Yasmani Grandal (X - X - X)
t7.new_ab()
t7.pitch_list("f f b f b s")
t7.out("K")

# 8. SD #3  Pedro Ciriaco (X - X - X)
t7.new_ab()
t7.pitch_list("s b f b")
t7.out("G5-3")

# 9. SD #5  Alexi Amarista (X - X - X)
t7.new_ab()
t7.pitch_list("c c c")
t7.out("!K")


# Bot 7th
# Pitching: SD #50 Nick Vincent
b7 = game.new_inning()

# Pitching change (SD): #50 Nick Vincent replaces #37 Edinson Volquez
b7.pitching_substitution(50)

# 9. BOS #10 Jose Iglesias (X - X - X)
b7.new_ab()
b7.pitch_list("b c f f")
b7.out("G3-1")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("b c b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
t8.pitching_substitution(36)

# 1. SD #11 Logan Forsythe (X - X - X)
t8.new_ab()
t8.pitch_list("c b b s f s")
t8.out("K")

# 2. SD #13 Chris Denorfia (X - X - X)
t8.new_ab()
t8.pitch_list("b f s s")
t8.out("K")

# 3. SD #18 Carlos Quentin (X - X - X)
t8.new_ab()
t8.pitch_list("s f b f f s")
t8.out("K")


# Bot 8th
# Pitching: SD #50 Nick Vincent
b8 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b")
b8.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("i i i i")
b8.reach("IBB")

# Pitching change (SD): #57 Luke Gregerson replaces #50 Nick Vincent
b8.pitching_substitution(57)

# 5. BOS #29 Daniel Nava (X - 15 - 34)
b8.new_ab(is_risp=True)
b8.pitch_list("c s s")
b8.out("K")

# 6. BOS #37 Mike Carp (X - 15 - 34)
b8.new_ab(is_risp=True)
b8.pitch_list("b b")
b8.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - 15 - 34)
b8.new_ab(is_risp=True)
b8.pitch_list("d c d c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# 4. SD #7  Chase Headley (X - X - X)
t9.new_ab()
t9.pitch_list("s s b f")
t9.out("G4-3")

# 5. SD #88 Kyle Blanks (X - X - X)
t9.new_ab()
t9.pitch_list("b s b")
t9.out("G1-3")

# 6. SD #15 Jesus Guzman (X - X - X)
t9.new_ab()
t9.pitch_list("b f s b b f b")
t9.reach("BB")

# 7. SD #12 Yasmani Grandal (X - X - 15)
t9.new_ab()
t9.pitch_list("b")
t9.out("F8")


# Bot 9th
# Pitching: SD #57 Luke Gregerson
b9 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #23 Brandon Snyder, batting 8th
b9.offensive_substitution(8, 5, "PH")

# 8. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("b s s b")
b9.hit(4)

# Winning team: BOS
# WP: BOS #19 Koji Uehara
game.winning_pitcher(19)

# Loser team: SD
# LP: SD #57 Luke Gregerson
game.losing_pitcher(57, is_away_team=True)

# print(game)
game.generate_scorecard()
