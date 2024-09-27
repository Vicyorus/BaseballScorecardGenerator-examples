import os
from baseball_scorecard.baseball_scorecard import Scorecard

# OAK @ BOS, 2013-04-23
# https://www.baseball-reference.com/boxes/BOS/BOS201304230.shtml
# https://www.mlb.com/gameday/athletics-vs-red-sox/2013/04/23/347044/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-23 18:36-21:46 (0:37 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "29,006",
        "temp": "42F, Drizzle",
        "wind": "18mph, In From CF",
        "away": {
            "team": "Oakland Athletics",
            "starter": 40,
            "roster": {
                # Lineup
                4: "Coco Crisp",
                5: "John Jaso",
                15: "Seth Smith",
                8: "Jed Lowrie",
                37: "Brandon Moss",
                20: "Josh Donaldson",
                16: "Josh Reddick",
                25: "Chris Young",
                28: "Eric Sogard",
                # Starting pitcher
                40: "Bartolo Colon",
                # Bench
                12: "Andy Parrino",
                36: "Derek Norris",
                53: "Casper Wells",
                7: "Nate Freiman",
                # Bullpen
                50: "Grant Balfour",
                64: "A.J. Griffin",
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
                [5, "2"],
                [15, "0"],
                [8, "6"],
                [37, "3"],
                [20, "5"],
                [16, "9"],
                [25, "7"],
                [28, "4"],
            ],
            "bench": [
                [12, "SS"],
                [36, "C"],
                [53, "RF"],
                [7, "1B"],
            ],
            "bullpen": [50, 64, 60, 11, 48, 62, 49, 57, 47, 13, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 91,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                # Starting pitcher
                91: "Alfredo Aceves",
                # Bench
                37: "Mike Carp",
                34: "David Ortiz",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                35: "Steven Wright",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [29, "7"],
                [16, "5"],
                [39, "2"],
                [5, "0"],
                [7, "6"],
            ],
            "bench": [
                [37, "1B"],
                [34, "DH"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 35, 40, 30, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Hunter Wendelstedt",
            "1B": "Jerry Layne",
            "2B": "Greg Gibson",
            "3B": "Mike Estabrook",
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
# Pitching: BOS #91 Alfredo Aceves
t1 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
t1.new_ab()
t1.pitch_list("c s s")
t1.out("K")

# 2. OAK #5  John Jaso (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("L3")

# 3. OAK #15 Seth Smith (X - X - X)
t1.new_ab()
t1.pitch_list("c t c")
t1.out("!K")


# Bot 1st
# Pitching: OAK #40 Bartolo Colon
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.out("F7")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b")
b1.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.hit(1)

# 4. BOS #12 Mike Napoli (X - X - 15)
b1.new_ab()
b1.pitch_list("c 1 s f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #91 Alfredo Aceves
t2 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
t2.new_ab()
t2.out("F8")

# 5. OAK #37 Brandon Moss (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(2, "20 BB")

# 6. OAK #20 Josh Donaldson (X - X - 37)
t2.new_ab()
t2.pitch_list("b f b f 1 b f d")
t2.reach("BB")

# 7. OAK #16 Josh Reddick (X - 37 - 20)
t2.new_ab()
t2.pitch_list("c d c")
t2.out("F8")

# 8. OAK #25 Chris Young (X - 37 - 20)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("P4")


# Bot 2nd
# Pitching: OAK #40 Bartolo Colon
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.out("F8")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("b c c s")
b2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("l f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #91 Alfredo Aceves
t3 = game.new_inning()

# 9. OAK #28 Eric Sogard (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "4 1B")
t3.advance(3, "5 BB")
t3.advance(4, "15 BB")

# 1. OAK #4  Coco Crisp (X - X - 28)
t3.new_ab()
t3.pitch_list("l 1 b s")
t3.hit(1)
t3.advance(2, "5 BB")
t3.advance(3, "15 BB")
t3.advance(4, "37 1B")

# 2. OAK #5  John Jaso (X - 28 - 4)
t3.new_ab()
t3.pitch_list("c b b f b f d")
t3.reach("BB")
t3.advance(2, "15 BB")
t3.advance(4, "37 1B")

# 3. OAK #15 Seth Smith (28 - 4 - 5)
t3.new_ab()
t3.pitch_list("b b b c f f b")
t3.reach("BB", rbis=1)
t3.advance(2, "37 1B")
t3.advance(3, "20 BLK")
t3.advance(4, "20 SF8")

# 4. OAK #8  Jed Lowrie (4 - 5 - 15)
t3.new_ab()
t3.pitch_list("f f c")
t3.out("!K")

# 5. OAK #37 Brandon Moss (4 - 5 - 15)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1, rbis=2)
t3.advance(2, "20 BLK")
t3.advance(4, "16 E1")

# 6. OAK #20 Josh Donaldson (X - 15 - 37)
t3.new_ab()
t3.pitch_list("d n c")
t3.balk()
t3.out("SF8", rbis=1)

# 7. OAK #16 Josh Reddick (X - 37 - X)
t3.new_ab()
t3.pitch_list("c c")
t3.hit(1, rbis=1)
t3.error(1)
t3.advance(2, "E1")
t3.advance(3, "25 BLK")
t3.advance("U", "25 E5")

# 8. OAK #25 Chris Young (X - 16 - X)
t3.new_ab()
t3.pitch_list("b f c n b")
t3.balk()
t3.error(5)
t3.reach("E5")

# 9. OAK #28 Eric Sogard (X - X - 25)
t3.new_ab()
t3.pitch_list("c 1 f b")
t3.out("G1-3")


# Bot 3rd
# Pitching: OAK #40 Bartolo Colon
b3 = game.new_inning()

# 8. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("c b c b")
b3.out("L6")

# 9. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b c b c")
b3.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b c c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #91 Alfredo Aceves
t4 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G4-3")

# 2. OAK #5  John Jaso (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.hit(2)
t4.advance(4, "15 HR")

# 3. OAK #15 Seth Smith (X - 5 - X)
t4.new_ab()
t4.hit(4, rbis=2)

# 4. OAK #8  Jed Lowrie (X - X - X)
t4.new_ab()
t4.pitch_list("c b c")
t4.hit(1)
t4.thrown_out(2, "37 DP4-6-3", 2, 35)

# Pitching change (BOS): #35 Steven Wright replaces #91 Alfredo Aceves
t4.pitching_substitution(35)

# 5. OAK #37 Brandon Moss (X - X - 8)
t4.new_ab()
t4.pitch_list("b f f")
t4.out("DP4-6-3")


# Bot 4th
# Pitching: OAK #40 Bartolo Colon
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("L4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c f b")
b4.out("G4-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #35 Steven Wright
t5 = game.new_inning()

# 6. OAK #20 Josh Donaldson (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "25 BB")
t5.advance(3, "28 BB")
t5.advance(4, "4 2B")

# 7. OAK #16 Josh Reddick (X - X - 20)
t5.new_ab()
t5.pitch_list("b c s c")
t5.out("!K")

# 8. OAK #25 Chris Young (X - X - 20)
t5.new_ab()
t5.pitch_list("b b c f b d")
t5.reach("BB")
t5.advance(2, "28 BB")
t5.advance(4, "4 2B")

# 9. OAK #28 Eric Sogard (X - 20 - 25)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.advance(3, "4 2B")
t5.advance(4, "5 1B")

# 1. OAK #4  Coco Crisp (20 - 25 - 28)
t5.new_ab()
t5.pitch_list("c s b")
t5.hit(2, rbis=2)
t5.advance(4, "5 1B")

# 2. OAK #5  John Jaso (28 - 4 - X)
t5.new_ab()
t5.pitch_list("c b c")
t5.hit(1, rbis=2)
t5.advance(2, "15 PB")
t5.thrown_out(3, "15 FC1-6-5", 2, 35)

# 3. OAK #15 Seth Smith (X - X - 5)
t5.new_ab()
t5.pitch_list("f b")
t5.pb()
t5.reach("FC1-6-5")

# 4. OAK #8  Jed Lowrie (X - X - 15)
t5.new_ab()
t5.pitch_list("b b c")
t5.out("F8")


# Bot 5th
# Pitching: OAK #40 Bartolo Colon
b5 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b c")
b5.out("G4-3")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.out("F9")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(2, "5 1B")

# 8. BOS #5  Jonny Gomes (X - X - 39)
b5.new_ab()
b5.pitch_list("c f b")
b5.hit(1)

# 9. BOS #7  Stephen Drew (X - 39 - 5)
b5.new_ab()
b5.out("P6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #35 Steven Wright
t6 = game.new_inning()

# 5. OAK #37 Brandon Moss (X - X - X)
t6.new_ab()
t6.pitch_list("b f b b c f b")
t6.reach("BB")
t6.advance(2, "20 BB")
t6.advance(4, "16 2B")

# 6. OAK #20 Josh Donaldson (X - X - 37)
t6.new_ab()
t6.pitch_list("b b b c f b")
t6.reach("BB")
t6.advance(3, "16 2B")

# 7. OAK #16 Josh Reddick (X - 37 - 20)
t6.new_ab()
t6.pitch_list("c")
t6.hit(2, rbis=1)

# 8. OAK #25 Chris Young (20 - 16 - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F9")

# 9. OAK #28 Eric Sogard (20 - 16 - X)
t6.new_ab()
t6.pitch_list("c f b c")
t6.out("!K")

# Offensive change (OAK): Pinch-hitter #53 Casper Wells replaces #4 Coco Crisp, batting 1st
t6.offensive_substitution(1, 53, "PH")

# 1. OAK #53 Casper Wells (20 - 16 - X)
t6.new_ab()
t6.out("F8")


# Bot 6th
# Pitching: OAK #40 Bartolo Colon
b6 = game.new_inning()

# Defensive switch (OAK): #53 Casper Wells moves to LF
b6.defensive_switch(53, "7")

# Defensive switch (OAK): #25 Chris Young moves to CF
b6.defensive_switch(25, "8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b f b b b")
b6.reach("BB")
b6.advance(2, "18 G4-3")
b6.advance(3, "15 G5-3")

# 2. BOS #18 Shane Victorino (X - X - 2)
b6.new_ab()
b6.pitch_list("c")
b6.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G5-3")

# 4. BOS #12 Mike Napoli (2 - X - X)
b6.new_ab()
b6.pitch_list("b c c b")
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# Defensive change (BOS): #23 Pedro Ciriaco replaces #15 Dustin Pedroia (2B), playing 2B, batting 3rd
t7.defensive_substitution(3, 23, "4")

# Defensive change (BOS): #37 Mike Carp replaces #12 Mike Napoli (1B), playing LF, batting 4th
t7.defensive_substitution(4, 37, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
t7.defensive_switch(29, "3")

# 2. OAK #5  John Jaso (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(2, "37 1B")

# 3. OAK #15 Seth Smith (X - X - 5)
t7.new_ab()
t7.pitch_list("b s f")
t7.out("F7")

# 4. OAK #8  Jed Lowrie (X - X - 5)
t7.new_ab()
t7.pitch_list("c c s")
t7.out("K")

# 5. OAK #37 Brandon Moss (X - X - 5)
t7.new_ab()
t7.pitch_list("s c f d b f b")
t7.hit(1)

# 6. OAK #20 Josh Donaldson (X - 5 - 37)
t7.new_ab()
t7.pitch_list("b f f b f d t")
t7.out("KT")


# Bot 7th
# Pitching: OAK #40 Bartolo Colon
b7 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c b c f s")
b7.out("K")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("c s f c")
b7.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b c f b f s")
b7.out("K")

# Winning team: OAK
# WP: OAK #40 Bartolo Colon
game.winning_pitcher(40, is_away_team=True)

# Loser team: BOS
# LP: BOS #91 Alfredo Aceves
game.losing_pitcher(91)

# print(game)
game.generate_scorecard()
