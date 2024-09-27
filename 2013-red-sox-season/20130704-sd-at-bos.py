import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SD @ BOS, 2013-07-04
# https://www.baseball-reference.com/boxes/BOS/BOS201307040.shtml
# https://www.mlb.com/gameday/padres-vs-red-sox/2013/07/04/348020/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-04 13:38-16:59",
        "at": "Fenway Park, Boston, MA",
        "att": "37,607",
        "temp": "91F, Sunny",
        "wind": "12mph, Out To CF",
        "away": {
            "team": "San Diego Padres",
            "starter": 53,
            "roster": {
                # Lineup
                11: "Logan Forsythe",
                25: "Will Venable",
                18: "Carlos Quentin",
                7: "Chase Headley",
                15: "Jesus Guzman",
                14: "Mark Kotsay",
                4: "Nick Hundley",
                5: "Alexi Amarista",
                3: "Pedro Ciriaco",
                # Starting pitcher
                53: "Eric Stults",
                # Bench
                12: "Yasmani Grandal",
                13: "Chris Denorfia",
                88: "Kyle Blanks",
                # Bullpen
                16: "Huston Street",
                46: "Tim Stauffer",
                55: "Dale Thayer",
                41: "Robbie Erlin",
                26: "Burch Smith",
                50: "Nick Vincent",
                37: "Edinson Volquez",
                38: "Tyson Ross",
                34: "Andrew Cashner",
                54: "Joe Thatcher",
                21: "Jason Marquis",
                57: "Luke Gregerson",
            },
            "lefties": [53, 41, 54],
            "lineup": [
                [11, "4"],
                [25, "9"],
                [18, "7"],
                [7, "5"],
                [15, "3"],
                [14, "0"],
                [4, "2"],
                [5, "8"],
                [3, "6"],
            ],
            "bench": [
                [12, "C"],
                [13, "RF"],
                [88, "LF"],
            ],
            "bullpen": [16, 46, 55, 41, 26, 50, 37, 38, 34, 54, 21, 57],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 64,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                23: "Brandon Snyder",
                20: "Ryan Lavarnway",
                10: "Jose Iglesias",
                # Starting pitcher
                64: "Allen Webster",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                76: "Jonathan Diaz",
                29: "Daniel Nava",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
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
                [23, "5"],
                [20, "2"],
                [10, "6"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [76, "SS"],
                [29, "LF"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 19, 31, 36, 22, 46],
        },
        "umpires": {
            "HP": "Dana DeMuth",
            "1B": "Angel Hernandez",
            "2B": "Paul Nauert",
            "3B": "Doug Eddings",
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
# Pitching: BOS #64 Allen Webster
t1 = game.new_inning()

# 1. SD #11 Logan Forsythe (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("L8")

# 2. SD #25 Will Venable (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b f b")
t1.reach("BB")

# 3. SD #18 Carlos Quentin (X - X - 25)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 4. SD #7  Chase Headley (X - X - 25)
t1.new_ab()
t1.pitch_list("b b")
t1.out("F8")


# Bot 1st
# Pitching: SD #53 Eric Stults
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(3, "18 2B")
b1.advance(4, "15 2B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("b b c")
b1.hit(2)
b1.advance(4, "15 2B")

# 3. BOS #15 Dustin Pedroia (2 - 18 - X)
b1.new_ab()
b1.pitch_list("c b b f f f")
b1.hit(2, rbis=2)
b1.advance(3, "34 G4-3")
b1.thrown_out(3, "12 DP1-5", 3, 53)

# 4. BOS #34 David Ortiz (X - 15 - X)
b1.new_ab()
b1.pitch_list("f b b s b")
b1.out("G4-3")

# 5. BOS #12 Mike Napoli (15 - X - X)
b1.new_ab()
b1.pitch_list("c t f b b")
b1.out("DP1-5")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #64 Allen Webster
t2 = game.new_inning()

# 5. SD #15 Jesus Guzman (X - X - X)
t2.new_ab()
t2.pitch_list("s c b")
t2.hit(1)

# 6. SD #14 Mark Kotsay (X - X - 15)
t2.new_ab()
t2.pitch_list("f")
t2.out("F9")

# 7. SD #4  Nick Hundley (X - X - 15)
t2.new_ab()
t2.out("F8")

# 8. SD #5  Alexi Amarista (X - X - 15)
t2.new_ab()
t2.pitch_list("b")
t2.out("G1")


# Bot 2nd
# Pitching: SD #53 Eric Stults
b2 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("b c f f b b")
b2.out("P5")

# 7. BOS #23 Brandon Snyder (X - X - X)
b2.new_ab()
b2.pitch_list("c s b")
b2.hit(4)

# 8. BOS #20 Ryan Lavarnway (X - X - X)
b2.new_ab()
b2.pitch_list("c c f")
b2.out("G6-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("b c f b f f b")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #64 Allen Webster
t3 = game.new_inning()

# 9. SD #3  Pedro Ciriaco (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "11 HBP")
t3.advance(3, "25 1B")
t3.advance(4, "7 SF8")

# 1. SD #11 Logan Forsythe (X - X - 3)
t3.new_ab()
t3.pitch_list("c b 1 1 f f b")
t3.reach("HBP")
t3.advance(2, "25 1B")
t3.advance(3, "15 BB")

# 2. SD #25 Will Venable (X - 3 - 11)
t3.new_ab()
t3.pitch_list("b c")
t3.hit(1)
t3.advance(2, "15 BB")

# 3. SD #18 Carlos Quentin (3 - 11 - 25)
t3.new_ab()
t3.out("F7")

# 4. SD #7  Chase Headley (3 - 11 - 25)
t3.new_ab()
t3.out("SF8", rbis=1)

# 5. SD #15 Jesus Guzman (X - 11 - 25)
t3.new_ab()
t3.pitch_list("d s s f b f b b")
t3.reach("BB")

# 6. SD #14 Mark Kotsay (11 - 25 - 15)
t3.new_ab()
t3.pitch_list("d s")
t3.out("G5-3")


# Bot 3rd
# Pitching: SD #53 Eric Stults
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("b c b f f 1 b")
b3.out("L7")

# 4. BOS #34 David Ortiz (X - X - 18)
b3.new_ab()
b3.out("L9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #64 Allen Webster
t4 = game.new_inning()

# 7. SD #4  Nick Hundley (X - X - X)
t4.new_ab()
t4.pitch_list("f f b f b b")
t4.out("P3")

# 8. SD #5  Alexi Amarista (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("F9")

# 9. SD #3  Pedro Ciriaco (X - X - X)
t4.new_ab()
t4.out("G6-3")


# Bot 4th
# Pitching: SD #53 Eric Stults
b4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.advance(2, "20 1B")
b4.advance(4, "10 2B")

# 6. BOS #5  Jonny Gomes (X - X - 12)
b4.new_ab()
b4.pitch_list("c d")
b4.out("L8")

# 7. BOS #23 Brandon Snyder (X - X - 12)
b4.new_ab()
b4.pitch_list("s b b c")
b4.out("F9")

# 8. BOS #20 Ryan Lavarnway (X - X - 12)
b4.new_ab()
b4.pitch_list("d")
b4.hit(1)
b4.advance(3, "10 2B")

# 9. BOS #10 Jose Iglesias (X - 12 - 20)
b4.new_ab()
b4.pitch_list("b c c")
b4.hit(2, rbis=1)

# 1. BOS #2  Jacoby Ellsbury (20 - 10 - X)
b4.new_ab()
b4.pitch_list("c")
b4.reach("HBP")

# 2. BOS #18 Shane Victorino (20 - 10 - 2)
b4.new_ab()
b4.pitch_list("b c f f")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #64 Allen Webster
t5 = game.new_inning()

# 1. SD #11 Logan Forsythe (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b b c")
t5.out("!K")

# 2. SD #25 Will Venable (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(2)
t5.advance(4, "15 1B")

# 3. SD #18 Carlos Quentin (X - 25 - X)
t5.new_ab()
t5.pitch_list("b b f s s")
t5.out("K")

# 4. SD #7  Chase Headley (X - 25 - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.advance(3, "15 1B")

# 5. SD #15 Jesus Guzman (X - 25 - 7)
t5.new_ab()
t5.hit(1, rbis=1)

# 6. SD #14 Mark Kotsay (7 - X - 15)
t5.new_ab()
t5.out("F7")


# Bot 5th
# Pitching: SD #53 Eric Stults
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c")
b5.hit(1)
b5.thrown_out(2, "12 CS", 2, 38)

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.pitch_list("c")
b5.out("F8")

# Pitching change (SD): #38 Tyson Ross replaces #53 Eric Stults
b5.pitching_substitution(38)

# 5. BOS #12 Mike Napoli (X - X - 15)
b5.new_ab()
b5.pitch_list("b s s f")
b5.hit(2)
b5.advance(4, "5 1B")

# 6. BOS #5  Jonny Gomes (X - 12 - X)
b5.new_ab()
b5.pitch_list("f")
b5.hit(1, rbis=1)

# 7. BOS #23 Brandon Snyder (X - X - 5)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #64 Allen Webster
t6 = game.new_inning()

# 7. SD #4  Nick Hundley (X - X - X)
t6.new_ab()
t6.pitch_list("f b s f s")
t6.out("K")

# 8. SD #5  Alexi Amarista (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c")
t6.hit(1)
t6.thrown_out(1, "3 DP5-3", 3, 64)

# 9. SD #3  Pedro Ciriaco (X - X - 5)
t6.new_ab()
t6.pitch_list("c b 1 s f 1 d b")
t6.out("DP5-3")


# Bot 6th
# Pitching: SD #38 Tyson Ross
b6 = game.new_inning()

# 8. BOS #20 Ryan Lavarnway (X - X - X)
b6.new_ab()
b6.pitch_list("c c")
b6.hit(1)
b6.advance(2, "10 1B")
b6.advance(3, "2 1B")
b6.thrown_out(4, "18 FC3-2", 1, 38)

# 9. BOS #10 Jose Iglesias (X - X - 20)
b6.new_ab()
b6.pitch_list("b d c")
b6.hit(1)
b6.advance(2, "2 1B")
b6.advance(3, "18 FC3-2")
b6.advance(4, "34 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 20 - 10)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(1)
b6.advance(2, "18 FC3-2")
b6.advance(4, "34 1B")

# 2. BOS #18 Shane Victorino (20 - 10 - 2)
b6.new_ab()
b6.pitch_list("b b f b f f f")
b6.reach("FC3-2")
b6.advance(3, "34 1B")

# 3. BOS #15 Dustin Pedroia (10 - 2 - 18)
b6.new_ab()
b6.pitch_list("b b b c")
b6.out("IF6")

# 4. BOS #34 David Ortiz (10 - 2 - 18)
b6.new_ab()
b6.pitch_list("f b c f d f f b")
b6.hit(1, rbis=2)

# Pitching change (SD): #26 Burch Smith replaces #38 Tyson Ross
b6.pitching_substitution(26)

# 5. BOS #12 Mike Napoli (18 - X - 34)
b6.new_ab()
b6.pitch_list("c c")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #40 Andrew Bailey
t7 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #64 Allen Webster
t7.pitching_substitution(40)

# 1. SD #11 Logan Forsythe (X - X - X)
t7.new_ab()
t7.pitch_list("b b s f c")
t7.out("!K")

# 2. SD #25 Will Venable (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b s s")
t7.out("K")

# 3. SD #18 Carlos Quentin (X - X - X)
t7.new_ab()
t7.out("F9")


# Bot 7th
# Pitching: SD #26 Burch Smith
b7 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.hit(2)

# 7. BOS #23 Brandon Snyder (X - 5 - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")

# 8. BOS #20 Ryan Lavarnway (X - 5 - X)
b7.new_ab()
b7.pitch_list("b f s b s")
b7.out("K")

# 9. BOS #10 Jose Iglesias (X - 5 - X)
b7.new_ab()
b7.pitch_list("b f b t b")
b7.out("P4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #63 Alex Wilson
t8 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #40 Andrew Bailey
t8.pitching_substitution(63)

# Defensive change (BOS): #29 Daniel Nava replaces #18 Shane Victorino (RF), playing RF, batting 2nd
t8.defensive_substitution(2, 29, "9")

# 4. SD #7  Chase Headley (X - X - X)
t8.new_ab()
t8.pitch_list("c f b f s")
t8.out("K")

# 5. SD #15 Jesus Guzman (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(2)
t8.advance(3, "14 G3-1")

# 6. SD #14 Mark Kotsay (X - 15 - X)
t8.new_ab()
t8.pitch_list("b b t c b")
t8.out("G3-1")

# 7. SD #4  Nick Hundley (15 - X - X)
t8.new_ab()
t8.pitch_list("b b b c b")
t8.reach("BB")

# 8. SD #5  Alexi Amarista (15 - X - 4)
t8.new_ab()
t8.pitch_list("c s b b")
t8.out("G6-3")


# Bot 8th
# Pitching: SD #26 Burch Smith
b8 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(4)

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("f c b b f f f")
b8.out("G1-3")

# Offensive change (BOS): Pinch-hitter #76 Jonathan Diaz replaces #15 Dustin Pedroia, batting 3rd
b8.offensive_substitution(3, 76, "PH")

# 3. BOS #76 Jonathan Diaz (X - X - X)
b8.new_ab()
b8.pitch_list("b c b")
b8.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.hit(2)

# 5. BOS #12 Mike Napoli (X - 34 - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #63 Alex Wilson
t9 = game.new_inning()

# Defensive switch (BOS): #76 Jonathan Diaz moves to 2B
t9.defensive_switch(76, "4")

# 9. SD #3  Pedro Ciriaco (X - X - X)
t9.new_ab()
t9.pitch_list("c f b")
t9.out("P3")

# Pitching change (BOS): #32 Craig Breslow replaces #63 Alex Wilson
t9.pitching_substitution(32)

# 1. SD #11 Logan Forsythe (X - X - X)
t9.new_ab()
t9.hit(2)

# 2. SD #25 Will Venable (X - 11 - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F7")

# 3. SD #18 Carlos Quentin (X - 11 - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("L7")

# Winning team: BOS
# WP: BOS #64 Allen Webster
game.winning_pitcher(64)

# Loser team: SD
# LP: SD #53 Eric Stults
game.losing_pitcher(53, is_away_team=True)

# print(game)
game.generate_scorecard()
