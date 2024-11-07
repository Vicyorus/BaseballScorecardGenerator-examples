import os
from baseball_scorecard.baseball_scorecard import Scorecard

# OAK @ BOS, 2013-04-24
# https://www.baseball-reference.com/boxes/BOS/BOS201304240.shtml
# https://www.mlb.com/gameday/athletics-vs-red-sox/2013/04/24/347058/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-24 16:05-19:45",
        "at": "Fenway Park, Boston, MA",
        "att": "29,274",
        "temp": "69F, Sunny",
        "wind": "14mph, R To L",
        "away": {
            "team": "Oakland Athletics",
            "starter": 49,
            "roster": {
                # Lineup
                4: "Coco Crisp",
                36: "Derek Norris",
                15: "Seth Smith",
                8: "Jed Lowrie",
                20: "Josh Donaldson",
                37: "Brandon Moss",
                25: "Chris Young",
                7: "Nate Freiman",
                12: "Andy Parrino",
                # Starting pitcher
                49: "Brett Anderson",
                # Bench
                53: "Casper Wells",
                16: "Josh Reddick",
                28: "Eric Sogard",
                5: "John Jaso",
                # Bullpen
                50: "Grant Balfour",
                64: "A.J. Griffin",
                40: "Bartolo Colon",
                60: "Jesse Chavez",
                11: "Jarrod Parker",
                48: "Ryan Cook",
                62: "Sean Doolittle",
                57: "Tommy Milone",
                47: "Pat Neshek",
                13: "Jerry Blevins",
                44: "Chris Resop",
            },
            "lefties": [49, 62, 57, 13],
            "lineup": [
                [4, "8"],
                [36, "2"],
                [15, "7"],
                [8, "6"],
                [20, "5"],
                [37, "3"],
                [25, "9"],
                [7, "0"],
                [12, "4"],
            ],
            "bench": [
                [53, "RF"],
                [16, "RF"],
                [28, "2B"],
                [5, "C"],
            ],
            "bullpen": [50, 64, 40, 60, 11, 48, 62, 57, 47, 13, 44],
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
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                51: "Daniel Bard",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [23, "3B"],
            ],
            "bullpen": [63, 40, 30, 91, 59, 36, 11, 51, 19, 22, 46],
        },
        "umpires": {
            "HP": "Jerry Layne",
            "1B": "Greg Gibson",
            "2B": "Mike Estabrook",
            "3B": "Hunter Wendelstedt",
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

# 1. OAK #4  Coco Crisp (X - X - X)
t1.new_ab()
t1.pitch_list("c b b s b f b")
t1.reach("BB")
t1.thrown_out(2, "36 DP5-4-3", 1, 31)

# 2. OAK #36 Derek Norris (X - X - 4)
t1.new_ab()
t1.pitch_list("c")
t1.out("DP5-4-3")

# 3. OAK #15 Seth Smith (X - X - X)
t1.new_ab()
t1.pitch_list("b f b c b b")
t1.reach("BB")
t1.advance(2, "8 1B")

# 4. OAK #8  Jed Lowrie (X - X - 15)
t1.new_ab()
t1.pitch_list("b c f b")
t1.hit(1)
t1.thrown_out(2, "20 FC5-4", 3, 31)

# 5. OAK #20 Josh Donaldson (X - 15 - 8)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.reach("FC5-4")


# Bot 1st
# Pitching: OAK #49 Brett Anderson
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f c b s")
b1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c c b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 6. OAK #37 Brandon Moss (X - X - X)
t2.new_ab()
t2.pitch_list("c c f b b f f s")
t2.out("K")

# 7. OAK #25 Chris Young (X - X - X)
t2.new_ab()
t2.pitch_list("b s f f b b f b")
t2.reach("BB")
t2.advance(2, "12 SB")

# 8. OAK #7  Nate Freiman (X - X - 25)
t2.new_ab()
t2.out("F8")

# 9. OAK #12 Andy Parrino (X - X - 25)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b c s")
t2.out("K")


# Bot 2nd
# Pitching: OAK #49 Brett Anderson
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")

# 6. BOS #5  Jonny Gomes (X - X - 12)
b2.new_ab()
b2.pitch_list("c b f b f")
b2.out("F8")

# 7. BOS #16 Will Middlebrooks (X - X - 12)
b2.new_ab()
b2.pitch_list("1 b c b")
b2.out("P4")

# 8. BOS #7  Stephen Drew (X - X - 12)
b2.new_ab()
b2.pitch_list("d 1 f b c b t")
b2.out("KT")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
t3.new_ab()
t3.pitch_list("f c f b b f b f f")
t3.out("F9")

# 2. OAK #36 Derek Norris (X - X - X)
t3.new_ab()
t3.pitch_list("b f b f f")
t3.out("P4")

# 3. OAK #15 Seth Smith (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f c")
t3.out("!K")


# Bot 3rd
# Pitching: OAK #49 Brett Anderson
b3 = game.new_inning()

# 9. BOS #3  David Ross (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("f f f b")
b3.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b c c b f b c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
t4.new_ab()
t4.hit(1)
t4.thrown_out(2, "20 FC6-4", 1, 31)

# 5. OAK #20 Josh Donaldson (X - X - 8)
t4.new_ab()
t4.pitch_list("c b c")
t4.reach("FC6-4")
t4.advance(2, "37 1B")
t4.advance(4, "25 HR")

# 6. OAK #37 Brandon Moss (X - X - 20)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(4, "25 HR")

# 7. OAK #25 Chris Young (X - 20 - 37)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.hit(4, rbis=3)

# 8. OAK #7  Nate Freiman (X - X - X)
t4.new_ab()
t4.pitch_list("b b c c b b")
t4.reach("BB")
t4.thrown_out(2, "12 DP4-6-3", 2, 31)

# 9. OAK #12 Andy Parrino (X - X - 7)
t4.new_ab()
t4.out("DP4-6-3")


# Bot 4th
# Pitching: OAK #49 Brett Anderson
b4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.hit(2)
b4.advance(4, "12 2B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b s")
b4.hit(2, rbis=1)
b4.advance(3, "16 FC1-4")
b4.advance(4, "7 3B")

# 6. BOS #5  Jonny Gomes (X - 12 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b c b")
b4.reach("BB")
b4.thrown_out(2, "16 FC1-4", 2, 49)

# 7. BOS #16 Will Middlebrooks (X - 12 - 5)
b4.new_ab(is_risp=True)
b4.reach("FC1-4")
b4.advance(4, "7 3B")

# 8. BOS #7  Stephen Drew (12 - X - 16)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b")
b4.hit(3, rbis=2)

# 9. BOS #3  David Ross (7 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("s c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
t5.new_ab()
t5.out("G5-3")

# 2. OAK #36 Derek Norris (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b b b")
t5.reach("BB")
t5.thrown_out(2, "8 FC6-4", 3, 31)

# 3. OAK #15 Seth Smith (X - X - 36)
t5.new_ab()
t5.pitch_list("b s s f")
t5.out("L8")

# 4. OAK #8  Jed Lowrie (X - X - 36)
t5.new_ab()
t5.reach("FC6-4")


# Bot 5th
# Pitching: OAK #49 Brett Anderson
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("b c f")
b5.hit(1)
b5.advance(2, "18 SB")
b5.advance(4, "18 2B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b5.new_ab(is_risp=True)
b5.pitch_list("b c l f b f f")
b5.hit(2, rbis=1)
b5.advance(3, "15 1B")
b5.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b s b")
b5.hit(1)
b5.advance(2, "34 1B")
b5.advance(3, "12 HBP")
b5.advance(4, "29 1B")

# 4. BOS #34 David Ortiz (18 - X - 15)
b5.new_ab(is_risp=True)
b5.pitch_list("b b c")
b5.hit(1, rbis=1)
b5.advance(2, "12 HBP")
b5.advance(3, "29 1B")

# Pitching change (OAK): #44 Chris Resop replaces #49 Brett Anderson
b5.pitching_substitution(44)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b5.new_ab(is_risp=True)
b5.reach("HBP")
b5.advance(2, "29 1B")

# Offensive change (BOS): Pinch-hitter #29 Daniel Nava replaces #5 Jonny Gomes, batting 6th
b5.offensive_substitution(6, 29, "PH")

# 6. BOS #29 Daniel Nava (15 - 34 - 12)
b5.new_ab(is_risp=True)
b5.pitch_list("c b b c")
b5.hit(1, rbis=1)

# 7. BOS #16 Will Middlebrooks (34 - 12 - 29)
b5.new_ab(is_risp=True)
b5.out("F7")

# Pitching change (OAK): #13 Jerry Blevins replaces #44 Chris Resop
b5.pitching_substitution(13)

# 8. BOS #7  Stephen Drew (34 - 12 - 29)
b5.new_ab(is_risp=True)
b5.pitch_list("t t d b f s")
b5.out("K")

# 9. BOS #3  David Ross (34 - 12 - 29)
b5.new_ab(is_risp=True)
b5.pitch_list("b c f b f f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to LF
t6.defensive_switch(29, "7")

# 5. OAK #20 Josh Donaldson (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(2)
t6.advance(3, "12 1B")

# 6. OAK #37 Brandon Moss (X - 20 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("t s f s")
t6.out("K")

# 7. OAK #25 Chris Young (X - 20 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c s f f s")
t6.out("K")

# 8. OAK #7  Nate Freiman (X - 20 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b f s f b b")
t6.reach("BB")
t6.advance(2, "12 1B")

# 9. OAK #12 Andy Parrino (X - 20 - 7)
t6.new_ab(is_risp=True)
t6.hit(1)

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
t6.pitching_substitution(36)

# 1. OAK #4  Coco Crisp (20 - 7 - 12)
t6.new_ab(is_risp=True)
t6.pitch_list("b f d s")
t6.out("F7")


# Bot 6th
# Pitching: OAK #13 Jerry Blevins
b6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b b c")
b6.out("P6")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #36 Junichi Tazawa
t7 = game.new_inning()

# Defensive change (BOS): #37 Mike Carp replaces #18 Shane Victorino (RF), playing LF, batting 2nd
t7.defensive_substitution(2, 37, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
t7.defensive_switch(29, "9")

# 2. OAK #36 Derek Norris (X - X - X)
t7.new_ab()
t7.pitch_list("b c s b b")
t7.out("P4")

# 3. OAK #15 Seth Smith (X - X - X)
t7.new_ab()
t7.pitch_list("b t b")
t7.out("P4")

# 4. OAK #8  Jed Lowrie (X - X - X)
t7.new_ab()
t7.pitch_list("c s")
t7.hit(2)
t7.advance(4, "20 1B")

# 5. OAK #20 Josh Donaldson (X - 8 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b f b f f")
t7.hit(1, rbis=1)
t7.advance(2, "37 SB")

# Pitching change (BOS): #30 Andrew Miller replaces #36 Junichi Tazawa
t7.pitching_substitution(30)

# 6. OAK #37 Brandon Moss (X - X - 20)
t7.new_ab(is_risp=True)
t7.pitch_list("b c s b d s")
t7.out("K")


# Bot 7th
# Pitching: OAK #13 Jerry Blevins
b7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("s b b b")
b7.out("P5")

# Pitching change (OAK): #47 Pat Neshek replaces #13 Jerry Blevins
b7.pitching_substitution(47)

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("c s s")
b7.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c c b")
b7.hit(1)

# 7. BOS #16 Will Middlebrooks (X - X - 29)
b7.new_ab()
b7.pitch_list("b s f 1")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller
t8.pitching_substitution(19)

# 7. OAK #25 Chris Young (X - X - X)
t8.new_ab()
t8.pitch_list("b b f")
t8.hit(4)

# Offensive change (OAK): Pinch-hitter #16 Josh Reddick replaces #7 Nate Freiman, batting 8th
t8.offensive_substitution(8, 16, "PH")

# 8. OAK #16 Josh Reddick (X - X - X)
t8.new_ab()
t8.pitch_list("b b c s b s")
t8.out("K")

# Offensive change (OAK): Pinch-hitter #28 Eric Sogard replaces #12 Andy Parrino, batting 9th
t8.offensive_substitution(9, 28, "PH")

# 9. OAK #28 Eric Sogard (X - X - X)
t8.new_ab()
t8.pitch_list("b f f f b f f f c")
t8.out("!K")

# 1. OAK #4  Coco Crisp (X - X - X)
t8.new_ab()
t8.pitch_list("b b f c f")
t8.out("F8")


# Bot 8th
# Pitching: OAK #50 Grant Balfour
b8 = game.new_inning()

# Pitching change (OAK): #50 Grant Balfour replaces #47 Pat Neshek
b8.pitching_substitution(50)

# Defensive switch (OAK): #16 Josh Reddick moves to DH
b8.defensive_switch(16, "0")

# Defensive switch (OAK): #28 Eric Sogard moves to 2B
b8.defensive_switch(28, "4")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("c s b c")
b8.out("!K")

# 9. BOS #3  David Ross (X - X - X)
b8.new_ab()
b8.pitch_list("s b c b s")
b8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b b")
b8.reach("BB")
b8.advance(2, "37 BB")

# 2. BOS #37 Mike Carp (X - X - 2)
b8.new_ab()
b8.pitch_list("b b f s b b")
b8.reach("BB")
b8.thrown_out(2, "15 FC6-4", 3, 50)

# 3. BOS #15 Dustin Pedroia (X - 2 - 37)
b8.new_ab(is_risp=True)
b8.pitch_list("b f")
b8.reach("FC6-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
t9.pitching_substitution(40)

# Offensive change (OAK): Pinch-hitter #5 John Jaso replaces #36 Derek Norris, batting 2nd
t9.offensive_substitution(2, 5, "PH")

# 2. OAK #5  John Jaso (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f f b f s")
t9.out("K")

# 3. OAK #15 Seth Smith (X - X - X)
t9.new_ab()
t9.pitch_list("c f f s")
t9.out("K")

# 4. OAK #8  Jed Lowrie (X - X - X)
t9.new_ab()
t9.pitch_list("b f f b f b s")
t9.out("K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40)

# Loser team: OAK
# LP: OAK #49 Brett Anderson
game.losing_pitcher(49, is_away_team=True)

# print(game)
game.generate_scorecard()
