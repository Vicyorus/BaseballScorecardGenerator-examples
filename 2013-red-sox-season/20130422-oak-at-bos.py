import os
from baseball_scorecard.baseball_scorecard import Scorecard

# OAK @ BOS, 2013-04-22
# https://www.baseball-reference.com/boxes/BOS/BOS201304220.shtml
# https://www.mlb.com/gameday/athletics-vs-red-sox/2013/04/22/347029/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-22 18:38-22:07",
        "at": "Fenway Park, Boston, MA",
        "att": "28,926",
        "temp": "45F, Partly Cloudy",
        "wind": "18mph, In From RF",
        "away": {
            "team": "Oakland Athletics",
            "starter": 64,
            "roster": {
                # Lineup
                4: "Coco Crisp",
                25: "Chris Young",
                37: "Brandon Moss",
                8: "Jed Lowrie",
                36: "Derek Norris",
                20: "Josh Donaldson",
                16: "Josh Reddick",
                7: "Nate Freiman",
                12: "Andy Parrino",
                # Starting pitcher
                64: "A.J. Griffin",
                # Bench
                23: "Michael Taylor",
                15: "Seth Smith",
                28: "Eric Sogard",
                5: "John Jaso",
                # Bullpen
                50: "Grant Balfour",
                40: "Bartolo Colon",
                60: "Jesse Chavez",
                11: "Jarrod Parker",
                48: "Ryan Cook",
                62: "Sean Doolittle",
                49: "Brett Anderson",
                57: "Tommy Milone",
                47: "Pat Neshek",
                13: "Jerry Blevins",
                44: "Chris Resop",
            },
            "lefties": [62, 49, 57, 13],
            "lineup": [
                [4, "8"],
                [25, "7"],
                [37, "3"],
                [8, "6"],
                [36, "2"],
                [20, "5"],
                [16, "9"],
                [7, "0"],
                [12, "4"],
            ],
            "bench": [
                [23, "RF"],
                [15, "LF"],
                [28, "2B"],
                [5, "C"],
            ],
            "bullpen": [50, 40, 60, 11, 48, 62, 49, 57, 47, 13, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                35: "Steven Wright",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [16, "5"],
                [39, "2"],
                [7, "6"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 35, 40, 30, 91, 31, 59, 36, 11, 19, 46],
        },
        "umpires": {
            "HP": "Mike Estabrook",
            "1B": "Hunter Wendelstedt",
            "2B": "Jerry Layne",
            "3B": "Greg Gibson",
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
# Pitching: BOS #22 Felix Doubront
t1 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
t1.new_ab()
t1.pitch_list("b c c")
t1.out("G5-3")

# 2. OAK #25 Chris Young (X - X - X)
t1.new_ab()
t1.pitch_list("c c")
t1.out("L5")

# 3. OAK #37 Brandon Moss (X - X - X)
t1.new_ab()
t1.pitch_list("c b s b b f t")
t1.out("KT")


# Bot 1st
# Pitching: OAK #64 A.J. Griffin
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c f")
b1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b s")
b1.out("L4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b s f")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b s b")
t2.reach("BB")
t2.advance(3, "20 2B")
t2.advance(4, "16 WP")

# 5. OAK #36 Derek Norris (X - X - 8)
t2.new_ab()
t2.pitch_list("b c f c")
t2.out("!K")

# 6. OAK #20 Josh Donaldson (X - X - 8)
t2.new_ab()
t2.pitch_list("1 b")
t2.hit(2)
t2.advance(3, "16 WP")
t2.advance(4, "16 1B")

# 7. OAK #16 Josh Reddick (8 - 20 - X)
t2.new_ab()
t2.pitch_list("b f")
t2.wp()
t2.hit(1, rbis=1)

# 8. OAK #7  Nate Freiman (X - X - 16)
t2.new_ab()
t2.pitch_list("c")
t2.out("F7")

# 9. OAK #12 Andy Parrino (X - X - 16)
t2.new_ab()
t2.pitch_list("c 1 f f t")
t2.out("KT")


# Bot 2nd
# Pitching: OAK #64 A.J. Griffin
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("f b b f")
b2.hit(2)
b2.advance(4, "12 2B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(2, rbis=1)

# 6. BOS #29 Daniel Nava (X - 12 - X)
b2.new_ab()
b2.pitch_list("b c d")
b2.out("L7")

# 7. BOS #16 Will Middlebrooks (X - 12 - X)
b2.new_ab()
b2.pitch_list("f s b d t")
b2.out("KT")

# 8. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
t3.new_ab()
t3.pitch_list("c b s")
t3.out("G6-3")

# 2. OAK #25 Chris Young (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.out("G5-3")

# 3. OAK #37 Brandon Moss (X - X - X)
t3.new_ab()
t3.pitch_list("f s b f t")
t3.out("KT")


# Bot 3rd
# Pitching: OAK #64 A.J. Griffin
b3 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.hit(2)
b3.advance(3, "18 F8")

# 2. BOS #18 Shane Victorino (X - 2 - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("F8")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.out("P6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
t4.new_ab()
t4.out("P4")

# 5. OAK #36 Derek Norris (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b s t")
t4.out("KT")

# 6. OAK #20 Josh Donaldson (X - X - X)
t4.new_ab()
t4.pitch_list("f b b")
t4.out("G6-3")


# Bot 4th
# Pitching: OAK #64 A.J. Griffin
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("c f b c")
b4.out("!K")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s b f")
b4.reach("HBP")
b4.advance(3, "29 2B")
b4.advance(4, "16 HR")

# 6. BOS #29 Daniel Nava (X - X - 12)
b4.new_ab()
b4.hit(2)
b4.advance(4, "16 HR")

# 7. BOS #16 Will Middlebrooks (12 - 29 - X)
b4.new_ab()
b4.pitch_list("b b")
b4.hit(4, rbis=3)

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("b s s f s")
b4.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b4.new_ab()
b4.pitch_list("c f b f b")
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 7. OAK #16 Josh Reddick (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b c")
t5.out("!K")

# 8. OAK #7  Nate Freiman (X - X - X)
t5.new_ab()
t5.pitch_list("f f b b b b")
t5.reach("BB")
t5.advance(2, "12 1B")
t5.advance(3, "4 WP")
t5.advance(4, "25 SF8")

# 9. OAK #12 Andy Parrino (X - X - 7)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "4 WP")
t5.advance(3, "25 SF8")

# 1. OAK #4  Coco Crisp (X - 7 - 12)
t5.new_ab()
t5.pitch_list("b b b b")
t5.wp()
t5.reach("BB")
t5.advance(2, "37 SB")

# 2. OAK #25 Chris Young (7 - 12 - 4)
t5.new_ab()
t5.pitch_list("b")
t5.out("SF8", rbis=1)

# 3. OAK #37 Brandon Moss (12 - X - 4)
t5.new_ab()
t5.pitch_list("b 1 b f b c b")
t5.reach("BB")

# 4. OAK #8  Jed Lowrie (12 - 4 - 37)
t5.new_ab()
t5.pitch_list("f c b b b")
t5.out("F8")


# Bot 5th
# Pitching: OAK #64 A.J. Griffin
b5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.hit(1)
b5.error(4)
b5.advance(2, "15 E4")
b5.advance(3, "34 BB")
b5.advance("U", "12 HR")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b5.new_ab()
b5.pitch_list("s b s")
b5.reach("FC5")
b5.advance(2, "34 BB")
b5.advance(4, "12 HR")

# 4. BOS #34 David Ortiz (X - 18 - 15)
b5.new_ab()
b5.pitch_list("b s b b b")
b5.reach("BB")
b5.advance(4, "12 HR")

# 5. BOS #12 Mike Napoli (18 - 15 - 34)
b5.new_ab()
b5.pitch_list("c")
b5.hit(4, rbis=4)

# 6. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.error(3)
b5.reach("E3")
b5.thrown_out(2, "16 FC6-4", 1, 44)

# Pitching change (OAK): #44 Chris Resop replaces #64 A.J. Griffin
b5.pitching_substitution(44)

# 7. BOS #16 Will Middlebrooks (X - X - 29)
b5.new_ab()
b5.pitch_list("f b c 1 d")
b5.reach("FC6-4")
b5.advance("U", "39 2B")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 16)
b5.new_ab()
b5.pitch_list("b")
b5.hit(2, rbis=1)
b5.advance(3, "7 G3")

# 9. BOS #7  Stephen Drew (X - 39 - X)
b5.new_ab()
b5.pitch_list("c b f")
b5.out("G3")

# 1. BOS #2  Jacoby Ellsbury (39 - X - X)
b5.new_ab()
b5.pitch_list("c b b s b b")
b5.reach("BB")
b5.advance(2, "18 SB")

# 2. BOS #18 Shane Victorino (39 - X - 2)
b5.new_ab()
b5.pitch_list("c s d d b b")
b5.reach("BB")

# 3. BOS #15 Dustin Pedroia (39 - 2 - 18)
b5.new_ab()
b5.pitch_list("b f b b f")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 5. OAK #36 Derek Norris (X - X - X)
t6.new_ab()
t6.pitch_list("s f b s")
t6.out("K")

# 6. OAK #20 Josh Donaldson (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b s b")
t6.reach("BB")

# 7. OAK #16 Josh Reddick (X - X - 20)
t6.new_ab()
t6.pitch_list("t f b s")
t6.out("K")

# 8. OAK #7  Nate Freiman (X - X - 20)
t6.new_ab()
t6.pitch_list("b c")
t6.out("L7")


# Bot 6th
# Pitching: OAK #13 Jerry Blevins
b6 = game.new_inning()

# Pitching change (OAK): #13 Jerry Blevins replaces #44 Chris Resop
b6.pitching_substitution(13)

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("b f f f b s")
b6.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("c f s")
b6.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.out("P6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 9. OAK #12 Andy Parrino (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G6-3")

# 1. OAK #4  Coco Crisp (X - X - X)
t7.new_ab()
t7.pitch_list("c b c")
t7.out("L8")

# Pitching change (BOS): #59 Clayton Mortensen replaces #22 Felix Doubront
t7.pitching_substitution(59)

# 2. OAK #25 Chris Young (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G5-3")


# Bot 7th
# Pitching: OAK #62 Sean Doolittle
b7 = game.new_inning()

# Pitching change (OAK): #62 Sean Doolittle replaces #13 Jerry Blevins
b7.pitching_substitution(62)

# 7. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("b s s b s")
b7.out("K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("c c f s")
b7.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("f b s b f b f b")
b7.reach("BB")
b7.advance(2, "2 BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b7.new_ab()
b7.pitch_list("b s b b s f f b")
b7.reach("BB")

# Pitching change (OAK): #60 Jesse Chavez replaces #62 Sean Doolittle
b7.pitching_substitution(60)

# 2. BOS #18 Shane Victorino (X - 7 - 2)
b7.new_ab()
b7.pitch_list("c d")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #59 Clayton Mortensen
t8 = game.new_inning()

# 3. OAK #37 Brandon Moss (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c b")
t8.reach("BB")
t8.advance(2, "36 HBP")
t8.advance(4, "20 2B")

# 4. OAK #8  Jed Lowrie (X - X - 37)
t8.new_ab()
t8.pitch_list("s f s")
t8.out("K")

# 5. OAK #36 Derek Norris (X - X - 37)
t8.new_ab()
t8.pitch_list("b c s d f")
t8.reach("HBP")
t8.advance(4, "20 2B")

# 6. OAK #20 Josh Donaldson (X - 37 - 36)
t8.new_ab()
t8.pitch_list("d c d f")
t8.hit(2, rbis=2)
t8.advance(4, "16 2B")

# 7. OAK #16 Josh Reddick (X - 20 - X)
t8.new_ab()
t8.hit(2, rbis=1)
t8.advance(3, "28 L9")

# Pitching change (BOS): #63 Alex Wilson replaces #59 Clayton Mortensen
t8.pitching_substitution(63)

# Offensive change (OAK): Pinch-hitter #15 Seth Smith replaces #7 Nate Freiman, batting 8th
t8.offensive_substitution(8, 15, "PH")

# 8. OAK #15 Seth Smith (X - 16 - X)
t8.new_ab()
t8.pitch_list("f b c d b b")
t8.reach("BB")

# Pitching change (BOS): #36 Junichi Tazawa replaces #63 Alex Wilson
t8.pitching_substitution(36)

# Offensive change (OAK): Pinch-hitter #28 Eric Sogard replaces #12 Andy Parrino, batting 9th
t8.offensive_substitution(9, 28, "PH")

# 9. OAK #28 Eric Sogard (X - 16 - 15)
t8.new_ab()
t8.pitch_list("b f f b")
t8.out("L9")

# 1. OAK #4  Coco Crisp (16 - X - 15)
t8.new_ab()
t8.pitch_list("b f")
t8.out("G3")


# Bot 8th
# Pitching: OAK #60 Jesse Chavez
b8 = game.new_inning()

# Defensive switch (OAK): #15 Seth Smith moves to DH
b8.defensive_switch(15, "0")

# Defensive switch (OAK): #28 Eric Sogard moves to 2B
b8.defensive_switch(28, "4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("b f s f")
b8.out("P4")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("P5")

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b f c f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #36 Junichi Tazawa
t9.pitching_substitution(40)

# 2. OAK #25 Chris Young (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c b")
t9.reach("BB")
t9.advance(2, "5 DI")

# 3. OAK #37 Brandon Moss (X - X - 25)
t9.new_ab()
t9.pitch_list("c c b b f s")
t9.out("K")

# 4. OAK #8  Jed Lowrie (X - X - 25)
t9.new_ab()
t9.pitch_list("b b c f s")
t9.out("K")

# Offensive change (OAK): Pinch-hitter #5 John Jaso replaces #36 Derek Norris, batting 5th
t9.offensive_substitution(5, 5, "PH")

# 5. OAK #5  John Jaso (X - X - 25)
t9.new_ab()
t9.pitch_list("b c b c")
t9.out("G3")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40)

# Loser team: OAK
# LP: OAK #64 A.J. Griffin
game.losing_pitcher(64, is_away_team=True)

# print(game)
game.generate_scorecard()
