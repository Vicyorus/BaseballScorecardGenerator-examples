import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CLE, 2013-04-17
# https://www.baseball-reference.com/boxes/CLE/CLE201304170.shtml
# https://www.mlb.com/gameday/red-sox-vs-indians/2013/04/17/346953/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-17 19:05-22:29",
        "at": "Progressive Field, Cleveland, OH",
        "att": "10,282",
        "temp": "46F, Cloudy",
        "wind": "17mph, In From RF",
        "away": {
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
                7: "Stephen Drew",
                37: "Mike Carp",
                # Starting pitcher
                91: "Alfredo Aceves",
                # Bench
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                44: "Jackie Bradley Jr.",
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
                [12, "0"],
                [29, "7"],
                [16, "5"],
                [39, "2"],
                [7, "6"],
                [37, "3"],
            ],
            "bench": [
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
                [44, "CF"],
            ],
            "bullpen": [63, 35, 40, 30, 31, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Cleveland Indians",
            "starter": 63,
            "roster": {
                # Lineup
                23: "Michael Brantley",
                13: "Asdrúbal Cabrera",
                41: "Carlos Santana",
                33: "Nick Swisher",
                25: "Jason Giambi",
                12: "Mark Reynolds",
                46: "Cord Phelps",
                8: "Lonnie Chisenhall",
                11: "Drew Stubbs",
                # Starting pitcher
                63: "Justin Masterson",
                # Bench
                9: "Ryan Raburn",
                10: "Yan Gomes",
                22: "Jason Kipnis",
                4: "Mike Aviles",
                # Bullpen
                54: "Chris Perez",
                37: "Cody Allen",
                50: "Nick Hagadone",
                39: "Brett Myers",
                30: "Ubaldo Jiménez",
                27: "Bryan Shaw",
                34: "Zach McAllister",
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
                [33, "9"],
                [25, "0"],
                [12, "3"],
                [46, "4"],
                [8, "5"],
                [11, "8"],
            ],
            "bench": [
                [9, "LF"],
                [10, "C"],
                [22, "2B"],
                [4, "SS"],
            ],
            "bullpen": [54, 37, 50, 39, 30, 27, 34, 53, 38, 52, 28],
        },
        "umpires": {
            "HP": "Tim Timmons",
            "1B": "Mike Winters",
            "2B": "Mark Wegner",
            "3B": "Laz Diaz",
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
# Pitching: CLE #63 Justin Masterson
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "18 HBP")
t1.advance(3, "15 1B")
t1.advance(4, "12 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("b b f c")
t1.reach("HBP")
t1.advance(2, "15 1B")
t1.advance(4, "12 1B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.hit(1)
t1.advance(2, "12 1B")
t1.advance(4, "29 1B")

# 4. BOS #12 Mike Napoli (2 - 18 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.hit(1, rbis=2)
t1.advance(2, "29 1B")
t1.advance(3, "16 G6-3")
t1.thrown_out(4, "39 FC3-2", 2, 63)

# 5. BOS #29 Daniel Nava (X - 15 - 12)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.hit(1, rbis=1)
t1.advance(2, "16 G6-3")
t1.advance(3, "39 FC3-2")

# 6. BOS #16 Will Middlebrooks (X - 12 - 29)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("G6-3")

# 7. BOS #39 Jarrod Saltalamacchia (12 - 29 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("s b f d")
t1.reach("FC3-2")

# 8. BOS #7  Stephen Drew (29 - X - 39)
t1.new_ab(is_risp=True)
t1.pitch_list("c c f b f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #91 Alfredo Aceves
b1 = game.new_inning()

# 1. CLE #23 Michael Brantley (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b")
b1.out("L9")

# 2. CLE #13 Asdrúbal Cabrera (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("L7")

# 3. CLE #41 Carlos Santana (X - X - X)
b1.new_ab()
b1.pitch_list("c f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CLE #63 Justin Masterson
t2 = game.new_inning()

# 9. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(2)
t2.advance(3, "18 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 37 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b c c")
t2.hit(1)
t2.advance(2, "18 1B")

# 2. BOS #18 Shane Victorino (X - 37 - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c b")
t2.hit(1)

# 3. BOS #15 Dustin Pedroia (37 - 2 - 18)
t2.new_ab(is_risp=True)
t2.pitch_list("b f b s s")
t2.out("K")

# 4. BOS #12 Mike Napoli (37 - 2 - 18)
t2.new_ab(is_risp=True)
t2.pitch_list("b b b c")
t2.out("(F)P3")

# 5. BOS #29 Daniel Nava (37 - 2 - 18)
t2.new_ab(is_risp=True)
t2.pitch_list("c f f")
t2.out("L7")


# Bot 2nd
# Pitching: BOS #91 Alfredo Aceves
b2 = game.new_inning()

# 4. CLE #33 Nick Swisher (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f b")
b2.hit(1)
b2.advance(2, "12 G3")

# 5. CLE #25 Jason Giambi (X - X - 33)
b2.new_ab()
b2.pitch_list("b")
b2.out("P6")

# 6. CLE #12 Mark Reynolds (X - X - 33)
b2.new_ab()
b2.pitch_list("b c s f")
b2.out("G3")

# 7. CLE #46 Cord Phelps (X - 33 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("s b b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CLE #63 Justin Masterson
t3 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b")
t3.out("(F)F9")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("c c")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #91 Alfredo Aceves
b3 = game.new_inning()

# 8. CLE #8  Lonnie Chisenhall (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.hit(1)
b3.thrown_out(2, "9-6", 1, 91)

# 9. CLE #11 Drew Stubbs (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c f f b")
b3.reach("BB")
b3.advance(2, "23 SB")

# 1. CLE #23 Michael Brantley (X - X - 11)
b3.new_ab(is_risp=True)
b3.pitch_list("1 c c b b f f")
b3.out("G6-3")

# 2. CLE #13 Asdrúbal Cabrera (X - 11 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CLE #63 Justin Masterson
t4 = game.new_inning()

# 9. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("c b c f b b")
t4.hit(2)
t4.advance(3, "15 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 37 - X)
t4.new_ab(is_risp=True)
t4.out("L7")

# 2. BOS #18 Shane Victorino (X - 37 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c d")
t4.hit(1)
t4.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - 37 - 18)
t4.new_ab(is_risp=True)
t4.pitch_list("f f")
t4.hit(1)

# 4. BOS #12 Mike Napoli (37 - 18 - 15)
t4.new_ab(is_risp=True)
t4.pitch_list("b b f f f s")
t4.out("K")

# 5. BOS #29 Daniel Nava (37 - 18 - 15)
t4.new_ab(is_risp=True)
t4.pitch_list("f")
t4.out("G3")


# Bot 4th
# Pitching: BOS #91 Alfredo Aceves
b4 = game.new_inning()

# 3. CLE #41 Carlos Santana (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b")
b4.out("G3")

# 4. CLE #33 Nick Swisher (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b b")
b4.out("L7")

# 5. CLE #25 Jason Giambi (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CLE #63 Justin Masterson
t5 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("b c f s")
t5.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 8. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b b")
t5.reach("BB")
t5.advance(4, "37 3B")

# 9. BOS #37 Mike Carp (X - X - 7)
t5.new_ab()
t5.pitch_list("b")
t5.hit(3, rbis=1)

# 1. BOS #2  Jacoby Ellsbury (37 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b c b c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #91 Alfredo Aceves
b5 = game.new_inning()

# 6. CLE #12 Mark Reynolds (X - X - X)
b5.new_ab()
b5.out("(F)P3")

# 7. CLE #46 Cord Phelps (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("G1-3")

# 8. CLE #8  Lonnie Chisenhall (X - X - X)
b5.new_ab()
b5.pitch_list("c b c b b")
b5.hit(1)
b5.advance(3, "11 2B")

# 9. CLE #11 Drew Stubbs (X - X - 8)
b5.new_ab()
b5.pitch_list("c c b b f")
b5.hit(2)

# 1. CLE #23 Michael Brantley (8 - 11 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f b b b")
b5.reach("BB")

# 2. CLE #13 Asdrúbal Cabrera (8 - 11 - 23)
b5.new_ab(is_risp=True)
b5.pitch_list("f c d")
b5.out("L9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CLE #28 Corey Kluber
t6 = game.new_inning()

# Pitching change (CLE): #28 Corey Kluber replaces #63 Justin Masterson
t6.pitching_substitution(28)

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("c b b")
t6.hit(1)
t6.advance(3, "12 2B")
t6.advance(4, "29 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t6.new_ab()
t6.pitch_list("c f b 1 s")
t6.out("K")

# 4. BOS #12 Mike Napoli (X - X - 18)
t6.new_ab()
t6.pitch_list("f c")
t6.hit(2)
t6.advance(3, "29 1B")

# 5. BOS #29 Daniel Nava (18 - 12 - X)
t6.new_ab(is_risp=True)
t6.hit(1, rbis=1)
t6.thrown_out(2, "16 CS", 2, 28)

# 6. BOS #16 Will Middlebrooks (12 - X - 29)
t6.new_ab(is_risp=True)
t6.pitch_list("s")
t6.out("F9")


# Bot 6th
# Pitching: BOS #91 Alfredo Aceves
b6 = game.new_inning()

# 3. CLE #41 Carlos Santana (X - X - X)
b6.new_ab()
b6.pitch_list("b b s s b b")
b6.reach("BB")
b6.advance(4, "33 HR")

# 4. CLE #33 Nick Swisher (X - X - 41)
b6.new_ab()
b6.pitch_list("b f")
b6.hit(4, rbis=2)

# 5. CLE #25 Jason Giambi (X - X - X)
b6.new_ab()
b6.pitch_list("b b c s f")
b6.hit(4)

# 6. CLE #12 Mark Reynolds (X - X - X)
b6.new_ab()
b6.pitch_list("c s f")
b6.hit(2)
b6.advance(3, "8 F8")

# Pitching change (BOS): #36 Junichi Tazawa replaces #91 Alfredo Aceves
b6.pitching_substitution(36)

# 7. CLE #46 Cord Phelps (X - 12 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("s c b")
b6.out("G5-3")

# 8. CLE #8  Lonnie Chisenhall (X - 12 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c")
b6.out("F8")

# 9. CLE #11 Drew Stubbs (12 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c c b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CLE #53 Rich Hill
t7 = game.new_inning()

# Pitching change (CLE): #53 Rich Hill replaces #28 Corey Kluber
t7.pitching_substitution(53)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("c b c")
t7.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L9")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 9th
t7.offensive_substitution(9, 5, "PH")

# 9. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("c s b c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b7.defensive_switch(29, "3")

# Defensive change (BOS): #44 Jackie Bradley Jr. replaces #5 Jonny Gomes (PH), playing LF, batting 9th
b7.defensive_substitution(9, 44, "7")

# 1. CLE #23 Michael Brantley (X - X - X)
b7.new_ab()
b7.pitch_list("b c c b b s")
b7.out("K")

# 2. CLE #13 Asdrúbal Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("c b s c")
b7.out("!K")

# 3. CLE #41 Carlos Santana (X - X - X)
b7.new_ab()
b7.pitch_list("b b s f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CLE #53 Rich Hill
t8 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b f c b f f b")
t8.hit(1)
t8.advance(2, "18 WP")
t8.advance("U", "18 SAC1")

# Pitching change (CLE): #38 Joe Smith replaces #53 Rich Hill
t8.pitching_substitution(38)

# 2. BOS #18 Shane Victorino (X - X - 2)
t8.new_ab(is_risp=True)
t8.pitch_list("b b")
t8.wp()
t8.error(1)
t8.reach("SAC1")
t8.thrown_out(2, "12 DP3-6-3", 2, 38)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t8.new_ab()
t8.pitch_list("b f b 1 f c")
t8.out("!K")

# 4. BOS #12 Mike Napoli (X - X - 18)
t8.new_ab()
t8.pitch_list("c b b s b")
t8.out("DP3-6-3")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b8.pitching_substitution(19)

# 4. CLE #33 Nick Swisher (X - X - X)
b8.new_ab()
b8.pitch_list("c c b")
b8.out("G3")

# 5. CLE #25 Jason Giambi (X - X - X)
b8.new_ab()
b8.pitch_list("b c s s")
b8.out("K")

# 6. CLE #12 Mark Reynolds (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CLE #52 Vinnie Pestano
t9 = game.new_inning()

# Pitching change (CLE): #52 Vinnie Pestano replaces #38 Joe Smith
t9.pitching_substitution(52)

# 5. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.out("L9")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("c c f c")
t9.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")


# Bot 9th
# Pitching: BOS #40 Andrew Bailey
b9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
b9.pitching_substitution(40)

# 7. CLE #46 Cord Phelps (X - X - X)
b9.new_ab()
b9.pitch_list("b c c b f f f")
b9.out("F8")

# 8. CLE #8  Lonnie Chisenhall (X - X - X)
b9.new_ab()
b9.pitch_list("c b c s")
b9.out("K")

# 9. CLE #11 Drew Stubbs (X - X - X)
b9.new_ab()
b9.pitch_list("s c f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #91 Alfredo Aceves
game.winning_pitcher(91, is_away_team=True)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40, is_away_team=True)

# Loser team: CLE
# LP: CLE #63 Justin Masterson
game.losing_pitcher(63)

# print(game)
game.generate_scorecard()
