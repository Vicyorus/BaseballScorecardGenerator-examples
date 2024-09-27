import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CLE, 2013-04-18
# https://www.baseball-reference.com/boxes/CLE/CLE201304180.shtml
# https://www.mlb.com/gameday/red-sox-vs-indians/2013/04/18/346968/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-18 19:04-22:17",
        "at": "Progressive Field, Cleveland, OH",
        "att": "12,936",
        "temp": "81F, Partly Cloudy",
        "wind": "21mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                29: "Daniel Nava",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                23: "Pedro Ciriaco",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                3: "David Ross",
                37: "Mike Carp",
                16: "Will Middlebrooks",
                # Bullpen
                63: "Alex Wilson",
                35: "Steven Wright",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                91: "Alfredo Aceves",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
                11: "Clay Buchholz",
            },
            "lefties": [31, 30, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [29, "7"],
                [5, "0"],
                [39, "2"],
                [7, "6"],
                [23, "5"],
            ],
            "bench": [
                [3, "C"],
                [37, "1B"],
                [16, "3B"],
            ],
            "bullpen": [63, 35, 40, 30, 19, 91, 59, 36, 22, 46, 11],
        },
        "home": {
            "team": "Cleveland Indians",
            "starter": 34,
            "roster": {
                # Lineup
                23: "Michael Brantley",
                13: "Asdrúbal Cabrera",
                41: "Carlos Santana",
                33: "Nick Swisher",
                12: "Mark Reynolds",
                9: "Ryan Raburn",
                4: "Mike Aviles",
                46: "Cord Phelps",
                11: "Drew Stubbs",
                # Starting pitcher
                34: "Zach McAllister",
                # Bench
                10: "Yan Gomes",
                22: "Jason Kipnis",
                25: "Jason Giambi",
                8: "Lonnie Chisenhall",
                # Bullpen
                54: "Chris Perez",
                37: "Cody Allen",
                50: "Nick Hagadone",
                39: "Brett Myers",
                63: "Justin Masterson",
                30: "Ubaldo Jiménez",
                27: "Bryan Shaw",
                53: "Rich Hill",
                38: "Joe Smith",
                52: "Vinnie Pestano",
                28: "Corey Kluber",
            },
            "lefties": [50, 53],
            "lineup": [
                [23, "7"],
                [13, "6"],
                [41, "2"],
                [33, "3"],
                [12, "0"],
                [9, "9"],
                [4, "5"],
                [46, "4"],
                [11, "8"],
            ],
            "bench": [
                [10, "C"],
                [22, "2B"],
                [25, "1B"],
                [8, "3B"],
            ],
            "bullpen": [54, 37, 50, 39, 63, 30, 27, 53, 38, 52, 28],
        },
        "umpires": {
            "HP": "Mike Winters",
            "1B": "Mark Wegner",
            "2B": "Laz Diaz",
            "3B": "Tim Timmons",
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
# Pitching: CLE #34 Zach McAllister
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b f f f c")
t1.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b c b c")
t1.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b c c f b b f c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. CLE #23 Michael Brantley (X - X - X)
b1.new_ab()
b1.pitch_list("c b f s")
b1.out("K")

# 2. CLE #13 Asdrúbal Cabrera (X - X - X)
b1.new_ab()
b1.pitch_list("f b c b")
b1.out("F9")

# 3. CLE #41 Carlos Santana (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f b f")
b1.hit(1)

# 4. CLE #33 Nick Swisher (X - X - 41)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CLE #34 Zach McAllister
t2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("s b")
t2.hit(3)
t2.advance(4, "29 1B")

# 5. BOS #29 Daniel Nava (12 - X - X)
t2.new_ab()
t2.hit(1, rbis=1)
t2.thrown_out(2, "5 FC5-4", 1, 34)

# 6. BOS #5  Jonny Gomes (X - X - 29)
t2.new_ab()
t2.pitch_list("b b c c f")
t2.reach("FC5-4")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 5)
t2.new_ab()
t2.pitch_list("s s f")
t2.out("P5")

# 8. BOS #7  Stephen Drew (X - X - 5)
t2.new_ab()
t2.pitch_list("c b b c t")
t2.out("KT")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. CLE #12 Mark Reynolds (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c")
b2.hit(2)
b2.advance(3, "9 F9")
b2.advance(4, "4 G5-3")

# 6. CLE #9  Ryan Raburn (X - 12 - X)
b2.new_ab()
b2.pitch_list("b c b f f")
b2.out("F9")

# 7. CLE #4  Mike Aviles (12 - X - X)
b2.new_ab()
b2.pitch_list("f")
b2.out("G5-3", rbis=1)

# 8. CLE #46 Cord Phelps (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CLE #34 Zach McAllister
t3 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.thrown_out(2, "2 FC6-4", 1, 34)

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
t3.new_ab()
t3.pitch_list("b b c")
t3.reach("FC6-4")
t3.advance(2, "15 BB")
t3.advance(3, "12 SB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t3.new_ab()
t3.pitch_list("1 c f 1 1")
t3.out("(F)P5")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t3.new_ab()
t3.pitch_list("b b 1 1 b b")
t3.reach("BB")
t3.advance(2, "12 SB")

# 4. BOS #12 Mike Napoli (X - 2 - 15)
t3.new_ab()
t3.pitch_list("c b b c f f f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 9. CLE #11 Drew Stubbs (X - X - X)
b3.new_ab()
b3.pitch_list("s")
b3.out("F9")

# 1. CLE #23 Michael Brantley (X - X - X)
b3.new_ab()
b3.pitch_list("b t f b f b f c")
b3.out("!K")

# 2. CLE #13 Asdrúbal Cabrera (X - X - X)
b3.new_ab()
b3.pitch_list("b c b c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CLE #34 Zach McAllister
t4 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b c b f f b c")
t4.out("!K")

# 6. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("c c b f s")
t4.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("b s b f f b")
t4.hit(4)

# 8. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 3. CLE #41 Carlos Santana (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L7")

# 4. CLE #33 Nick Swisher (X - X - X)
b4.new_ab()
b4.pitch_list("f c b b f")
b4.out("G3-1")

# 5. CLE #12 Mark Reynolds (X - X - X)
b4.new_ab()
b4.pitch_list("b s b b t b")
b4.reach("BB")

# 6. CLE #9  Ryan Raburn (X - X - 12)
b4.new_ab()
b4.pitch_list("b f b b c")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CLE #34 Zach McAllister
t5 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("b b c")
t5.hit(2)
t5.advance(3, "18 1B")
t5.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - 2 - X)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(1)
t5.advance(3, "15 1B")

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
t5.new_ab()
t5.pitch_list("b c f f f b b")
t5.hit(1, rbis=1)
t5.advance(2, "12 SB")

# 4. BOS #12 Mike Napoli (18 - X - 15)
t5.new_ab()
t5.pitch_list("c s b b s")
t5.out("K")

# 5. BOS #29 Daniel Nava (18 - 15 - X)
t5.new_ab()
t5.pitch_list("b d i i")
t5.reach("IBB")

# 6. BOS #5  Jonny Gomes (18 - 15 - 29)
t5.new_ab()
t5.pitch_list("b f f")
t5.out("G3-1")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 7. CLE #4  Mike Aviles (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b f f")
b5.hit(2)
b5.advance(3, "46 G6-3")
b5.advance(4, "11 G4-3")

# 8. CLE #46 Cord Phelps (X - 4 - X)
b5.new_ab()
b5.out("G6-3")

# 9. CLE #11 Drew Stubbs (4 - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3", rbis=1)

# 1. CLE #23 Michael Brantley (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CLE #50 Nick Hagadone
t6 = game.new_inning()

# Pitching change (CLE): #50 Nick Hagadone replaces #34 Zach McAllister
t6.pitching_substitution(50)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.out("G5-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("s c b b s")
t6.out("K")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t6.new_ab()
t6.pitch_list("f b s b")
t6.out("F7")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 2. CLE #13 Asdrúbal Cabrera (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.hit(1)
b6.thrown_out(2, "41 DP6-4-3", 1, 31)

# 3. CLE #41 Carlos Santana (X - X - 13)
b6.new_ab()
b6.pitch_list("c")
b6.out("DP6-4-3")

# 4. CLE #33 Nick Swisher (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b")
b6.out("L8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CLE #50 Nick Hagadone
t7 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("f b b")
t7.hit(1)
t7.advance(2, "18 E4")
t7.advance(3, "15 F9")
t7.advance(4, "12 1B")

# Pitching change (CLE): #27 Bryan Shaw replaces #50 Nick Hagadone
t7.pitching_substitution(27)

# 2. BOS #18 Shane Victorino (X - X - 2)
t7.new_ab()
t7.pitch_list("b 1")
t7.error(4)
t7.reach("E4")
t7.advance(3, "12 1B")
t7.advance("U", "29 SF8")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t7.new_ab()
t7.pitch_list("b")
t7.out("F9")

# 4. BOS #12 Mike Napoli (2 - X - 18)
t7.new_ab()
t7.pitch_list("s f 1")
t7.hit(1, rbis=1)
t7.advance(2, "29 SF8")
t7.advance("U", "37 1B")

# 5. BOS #29 Daniel Nava (18 - X - 12)
t7.new_ab()
t7.pitch_list("b c")
t7.out("SF8", rbis=1)

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #5 Jonny Gomes, batting 6th
t7.offensive_substitution(6, 37, "PH")

# 6. BOS #37 Mike Carp (X - 12 - X)
t7.new_ab()
t7.pitch_list("c f")
t7.hit(1, rbis=1)
t7.advance(2, "T")

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
t7.new_ab()
t7.pitch_list("s f b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# Defensive switch (BOS): #37 Mike Carp moves to DH
b7.defensive_switch(37, "0")

# 5. CLE #12 Mark Reynolds (X - X - X)
b7.new_ab()
b7.pitch_list("b c s b f")
b7.out("L7")

# 6. CLE #9  Ryan Raburn (X - X - X)
b7.new_ab()
b7.pitch_list("b b f c b f f")
b7.out("G6-3")

# 7. CLE #4  Mike Aviles (X - X - X)
b7.new_ab()
b7.pitch_list("c c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CLE #27 Bryan Shaw
t8 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("L9")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t8.new_ab()
t8.pitch_list("c t s")
t8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b c s f")
t8.out("G3-1")


# Bot 8th
# Pitching: BOS #30 Andrew Miller
b8 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #31 Jon Lester
b8.pitching_substitution(30)

# 8. CLE #46 Cord Phelps (X - X - X)
b8.new_ab()
b8.pitch_list("b b c b f f c")
b8.out("!K")

# 9. CLE #11 Drew Stubbs (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b c b")
b8.reach("BB")
b8.advance(2, "23 1B")
b8.thrown_out(3, "13 FC5", 2, 30)

# 1. CLE #23 Michael Brantley (X - X - 11)
b8.new_ab()
b8.pitch_list("b b c c")
b8.hit(1)
b8.advance(2, "13 FC5")
b8.advance(4, "41 2B")

# 2. CLE #13 Asdrúbal Cabrera (X - 11 - 23)
b8.new_ab()
b8.pitch_list("c b s b")
b8.reach("FC5")
b8.advance(3, "41 2B")

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller
b8.pitching_substitution(19)

# 3. CLE #41 Carlos Santana (X - 23 - 13)
b8.new_ab()
b8.pitch_list("c b b s f")
b8.hit(2, rbis=1)

# 4. CLE #33 Nick Swisher (13 - 41 - X)
b8.new_ab()
b8.pitch_list("b f s b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CLE #54 Chris Perez
t9 = game.new_inning()

# Pitching change (CLE): #54 Chris Perez replaces #27 Bryan Shaw
t9.pitching_substitution(54)

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("b f f c")
t9.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c b f f b")
t9.out("L9")

# 4. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b c s f f f")
t9.out("L9")


# Bot 9th
# Pitching: BOS #40 Andrew Bailey
b9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
b9.pitching_substitution(40)

# 5. CLE #12 Mark Reynolds (X - X - X)
b9.new_ab()
b9.pitch_list("c b f f b s")
b9.out("K")

# 6. CLE #9  Ryan Raburn (X - X - X)
b9.new_ab()
b9.pitch_list("c s f")
b9.out("(F)P2")

# 7. CLE #4  Mike Aviles (X - X - X)
b9.new_ab()
b9.pitch_list("b f")
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31, is_away_team=True)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40, is_away_team=True)

# Loser team: CLE
# LP: CLE #34 Zach McAllister
game.losing_pitcher(34)

# print(game)
game.generate_scorecard()
