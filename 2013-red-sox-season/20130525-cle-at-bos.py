import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2013-05-25
# https://www.baseball-reference.com/boxes/BOS/BOS201305250.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2013/05/25/347467/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-25 13:39-17:03",
        "at": "Fenway Park, Boston, MA",
        "att": "36,504",
        "temp": "53F, Rain",
        "wind": "12mph, L To R",
        "away": {
            "team": "Cleveland Indians",
            "starter": 26,
            "roster": {
                # Lineup
                11: "Drew Stubbs",
                4: "Mike Aviles",
                13: "Asdrúbal Cabrera",
                33: "Nick Swisher",
                12: "Mark Reynolds",
                41: "Carlos Santana",
                10: "Yan Gomes",
                23: "Michael Brantley",
                9: "Ryan Raburn",
                # Starting pitcher
                26: "Scott Kazmir",
                # Bench
                24: "Michael Bourn",
                22: "Jason Kipnis",
                25: "Jason Giambi",
                # Bullpen
                32: "Matt Albers",
                54: "Chris Perez",
                37: "Cody Allen",
                51: "Scott Barnes",
                63: "Justin Masterson",
                30: "Ubaldo Jiménez",
                27: "Bryan Shaw",
                34: "Zach McAllister",
                53: "Rich Hill",
                38: "Joe Smith",
                52: "Vinnie Pestano",
                28: "Corey Kluber",
            },
            "lefties": [26, 51, 53],
            "lineup": [
                [11, "8"],
                [4, "4"],
                [13, "6"],
                [33, "3"],
                [12, "5"],
                [41, "0"],
                [10, "2"],
                [23, "7"],
                [9, "9"],
            ],
            "bench": [
                [24, "CF"],
                [22, "2B"],
                [25, "1B"],
            ],
            "bullpen": [32, 54, 37, 51, 63, 30, 27, 34, 53, 38, 52, 28],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                3: "David Ross",
                10: "Jose Iglesias",
                23: "Pedro Ciriaco",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                91: "Alfredo Aceves",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [3, "2"],
                [10, "6"],
                [23, "5"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 91, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Ron Kulpa",
            "1B": "Chris Guccione",
            "2B": "Phil Cuzzi",
            "3B": "Tom Hallion",
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

# 1. CLE #11 Drew Stubbs (X - X - X)
t1.new_ab()
t1.pitch_list("c b f s")
t1.out("K")

# 2. CLE #4  Mike Aviles (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G4-3")

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t1.new_ab()
t1.pitch_list("b c s b")
t1.hit(1)
t1.advance(2, "33 SB")
t1.advance(4, "33 2B")

# 4. CLE #33 Nick Swisher (X - X - 13)
t1.new_ab()
t1.pitch_list("b b")
t1.hit(2, rbis=1)

# 5. CLE #12 Mark Reynolds (X - 33 - X)
t1.new_ab()
t1.out("L7")


# Bot 1st
# Pitching: CLE #26 Scott Kazmir
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b b")
b1.reach("BB")
b1.advance(2, "34 BB")

# 2. BOS #5  Jonny Gomes (X - X - 2)
b1.new_ab()
b1.pitch_list("1 c b 1 b b f f")
b1.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b1.new_ab()
b1.pitch_list("b f 1 c b s")
b1.out("K")

# 4. BOS #34 David Ortiz (X - X - 2)
b1.new_ab()
b1.pitch_list("b c 1 b b b")
b1.reach("BB")

# 5. BOS #12 Mike Napoli (X - 2 - 34)
b1.new_ab()
b1.pitch_list("b b c")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 6. CLE #41 Carlos Santana (X - X - X)
t2.new_ab()
t2.pitch_list("b s b c f f s")
t2.out("K")

# 7. CLE #10 Yan Gomes (X - X - X)
t2.new_ab()
t2.out("G5-3")

# 8. CLE #23 Michael Brantley (X - X - X)
t2.new_ab()
t2.pitch_list("b c f")
t2.hit(1)

# 9. CLE #9  Ryan Raburn (X - X - 23)
t2.new_ab()
t2.out("(F)P2")


# Bot 2nd
# Pitching: CLE #26 Scott Kazmir
b2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c c t")
b2.out("KT")

# 7. BOS #3  David Ross (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c s c")
b2.out("!K")

# 8. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("c f f b")
b2.hit(1)
b2.advance(2, "23 BLK")
b2.advance(4, "23 1B")

# 9. BOS #23 Pedro Ciriaco (X - X - 10)
b2.new_ab()
b2.pitch_list("c s n b f")
b2.balk()
b2.hit(1, rbis=1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
b2.new_ab()
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 1. CLE #11 Drew Stubbs (X - X - X)
t3.new_ab()
t3.pitch_list("s b b b b")
t3.reach("BB")
t3.advance(2, "4 G5-3")
t3.advance(4, "13 2B")

# 2. CLE #4  Mike Aviles (X - X - 11)
t3.new_ab()
t3.pitch_list("b f c b b")
t3.out("G5-3")

# 3. CLE #13 Asdrúbal Cabrera (X - 11 - X)
t3.new_ab()
t3.pitch_list("c f d")
t3.hit(2, rbis=1)
t3.thrown_out(4, "33 7-2", 2, 31)

# 4. CLE #33 Nick Swisher (X - 13 - X)
t3.new_ab()
t3.pitch_list("c f f b b")
t3.hit(1)
t3.advance(2, "12 HBP")
t3.advance(4, "41 1B")

# 5. CLE #12 Mark Reynolds (X - X - 33)
t3.new_ab()
t3.pitch_list("s c")
t3.reach("HBP")
t3.error(5)
t3.advance(2, "41 1B")
t3.advance(3, "41 E5")

# 6. CLE #41 Carlos Santana (X - 33 - 12)
t3.new_ab()
t3.pitch_list("f b b")
t3.hit(1, rbis=1)
t3.advance(2, "E5")

# 7. CLE #10 Yan Gomes (12 - 41 - X)
t3.new_ab()
t3.pitch_list("c b b c f b f s")
t3.out("K")


# Bot 3rd
# Pitching: CLE #26 Scott Kazmir
b3 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f b b f")
b3.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
b3.new_ab()
b3.pitch_list("b b c f s")
b3.out("K")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 8. CLE #23 Michael Brantley (X - X - X)
t4.new_ab()
t4.hit(2)

# 9. CLE #9  Ryan Raburn (X - 23 - X)
t4.new_ab()
t4.pitch_list("s l b f f")
t4.out("G5-3")

# 1. CLE #11 Drew Stubbs (X - 23 - X)
t4.new_ab()
t4.pitch_list("b t f")
t4.out("P4")

# 2. CLE #4  Mike Aviles (X - 23 - X)
t4.new_ab()
t4.out("G4-3")


# Bot 4th
# Pitching: CLE #26 Scott Kazmir
b4 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b b f f b b")
b4.reach("BB")
b4.error(9)
b4.advance(3, "10 2B")
b4.advance(4, "10 E9")

# 7. BOS #3  David Ross (X - X - 29)
b4.new_ab()
b4.pitch_list("l 1 b s f s")
b4.out("K")

# 8. BOS #10 Jose Iglesias (X - X - 29)
b4.new_ab()
b4.pitch_list("c 1 f")
b4.hit(2)
b4.advance(3, "23 F8")

# 9. BOS #23 Pedro Ciriaco (X - 10 - X)
b4.new_ab()
b4.pitch_list("c f")
b4.out("F8")

# 1. BOS #2  Jacoby Ellsbury (10 - X - X)
b4.new_ab()
b4.pitch_list("c b t")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("F9")

# 4. CLE #33 Nick Swisher (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F9")

# 5. CLE #12 Mark Reynolds (X - X - X)
t5.new_ab()
t5.pitch_list("b s s")
t5.hit(1)

# 6. CLE #41 Carlos Santana (X - X - 12)
t5.new_ab()
t5.pitch_list("c f b s")
t5.out("K")


# Bot 5th
# Pitching: CLE #26 Scott Kazmir
b5 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("f c s")
b5.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("f f b b b f b")
b5.reach("BB")
b5.thrown_out(2, "34 FC2-6", 2, 26)

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.reach("FC2-6")
b5.advance(2, "12 1B")

# 5. BOS #12 Mike Napoli (X - X - 34)
b5.new_ab()
b5.pitch_list("1 b b c b")
b5.hit(1)

# 6. BOS #29 Daniel Nava (X - 34 - 12)
b5.new_ab()
b5.pitch_list("c b f b f")
b5.out("G1-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 7. CLE #10 Yan Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("c s b f c")
t6.out("!K")

# 8. CLE #23 Michael Brantley (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f b c")
t6.out("!K")

# 9. CLE #9  Ryan Raburn (X - X - X)
t6.new_ab()
t6.pitch_list("b f f s")
t6.out("K")


# Bot 6th
# Pitching: CLE #27 Bryan Shaw
b6 = game.new_inning()

# Pitching change (CLE): #27 Bryan Shaw replaces #26 Scott Kazmir
b6.pitching_substitution(27)

# 7. BOS #3  David Ross (X - X - X)
b6.new_ab()
b6.pitch_list("b c b s f b s")
b6.out("K")

# 8. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.hit(1)
b6.error(5)
b6.advance(2, "23 1B")
b6.advance(3, "23 E5")
b6.advance(4, "5 SF8")

# 9. BOS #23 Pedro Ciriaco (X - X - 10)
b6.new_ab()
b6.pitch_list("1 f")
b6.hit(1)
b6.advance(2, "E5")
b6.advance(3, "5 SF8")

# 1. BOS #2  Jacoby Ellsbury (10 - 23 - X)
b6.new_ab()
b6.pitch_list("i i i i")
b6.reach("IBB")

# 2. BOS #5  Jonny Gomes (10 - 23 - 2)
b6.new_ab()
b6.pitch_list("b")
b6.out("SF8", rbis=1)

# 3. BOS #15 Dustin Pedroia (23 - X - 2)
b6.new_ab()
b6.pitch_list("b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 1. CLE #11 Drew Stubbs (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G6-3")

# 2. CLE #4  Mike Aviles (X - X - X)
t7.new_ab()
t7.pitch_list("b c b")
t7.hit(1)
t7.advance(3, "13 1B")
t7.advance(4, "12 WP")

# 3. CLE #13 Asdrúbal Cabrera (X - X - 4)
t7.new_ab()
t7.pitch_list("b s s b")
t7.hit(1)
t7.advance(2, "12 SB")
t7.advance(3, "12 WP")

# 4. CLE #33 Nick Swisher (4 - X - 13)
t7.new_ab()
t7.out("L5")

# 5. CLE #12 Mark Reynolds (4 - X - 13)
t7.new_ab()
t7.pitch_list("f m b f b f b s")
t7.wp()
t7.out("K")


# Bot 7th
# Pitching: CLE #38 Joe Smith
b7 = game.new_inning()

# Pitching change (CLE): #38 Joe Smith replaces #27 Bryan Shaw
b7.pitching_substitution(38)

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("c c b b f s")
b7.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("c c b b f")
b7.out("F9")

# 6. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("b s c f b b b")
b7.reach("BB")

# 7. BOS #3  David Ross (X - X - 29)
b7.new_ab()
b7.pitch_list("f b f 1 s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
t8.pitching_substitution(36)

# 6. CLE #41 Carlos Santana (X - X - X)
t8.new_ab()
t8.pitch_list("c b b l s")
t8.out("K")

# 7. CLE #10 Yan Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("s c f f s")
t8.out("K")

# 8. CLE #23 Michael Brantley (X - X - X)
t8.new_ab()
t8.pitch_list("f c b")
t8.out("G3")


# Bot 8th
# Pitching: CLE #52 Vinnie Pestano
b8 = game.new_inning()

# Pitching change (CLE): #52 Vinnie Pestano replaces #38 Joe Smith
b8.pitching_substitution(52)

# Defensive switch (CLE): #11 Drew Stubbs moves to RF
b8.defensive_switch(11, "9")

# Defensive change (CLE): #24 Michael Bourn replaces #9 Ryan Raburn (RF), playing CF, batting 9th
b8.defensive_substitution(9, 24, "8")

# 8. BOS #10 Jose Iglesias (X - X - X)
b8.new_ab()
b8.pitch_list("b b c c")
b8.out("G4-3")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)
b8.advance(4, "37 2B")

# 1. BOS #2  Jacoby Ellsbury (X - 23 - X)
b8.new_ab()
b8.pitch_list("b f f b s")
b8.out("K")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #5 Jonny Gomes, batting 2nd
b8.offensive_substitution(2, 37, "PH")

# 2. BOS #37 Mike Carp (X - 23 - X)
b8.new_ab()
b8.hit(2, rbis=1)
b8.advance(4, "15 2B")

# 3. BOS #15 Dustin Pedroia (X - 37 - X)
b8.new_ab()
b8.pitch_list("c f")
b8.hit(2, rbis=1)
b8.advance(3, "12 BB")
b8.advance(4, "29 1B")

# 4. BOS #34 David Ortiz (X - 15 - X)
b8.new_ab()
b8.pitch_list("i i i i")
b8.reach("IBB")
b8.advance(2, "12 BB")
b8.advance(4, "29 1B")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b8.new_ab()
b8.pitch_list("s b b b c b")
b8.reach("BB")
b8.advance(3, "29 1B")

# 6. BOS #29 Daniel Nava (15 - 34 - 12)
b8.new_ab()
b8.hit(1, rbis=2)

# 7. BOS #3  David Ross (12 - X - 29)
b8.new_ab()
b8.pitch_list("s b c t")
b8.out("KT")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #36 Junichi Tazawa
t9.pitching_substitution(40)

# Defensive switch (BOS): #37 Mike Carp moves to LF
t9.defensive_switch(37, "7")

# 9. CLE #24 Michael Bourn (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "13 DI")

# Offensive change (CLE): Pinch-hitter #22 Jason Kipnis replaces #11 Drew Stubbs, batting 1st
t9.offensive_substitution(1, 22, "PH")

# 1. CLE #22 Jason Kipnis (X - X - 24)
t9.new_ab()
t9.pitch_list("c b b f d s")
t9.out("K")

# 2. CLE #4  Mike Aviles (X - X - 24)
t9.new_ab()
t9.pitch_list("b c c")
t9.out("(F)P3")

# 3. CLE #13 Asdrúbal Cabrera (X - X - 24)
t9.new_ab()
t9.pitch_list("c c")
t9.out("F8")

# Winning team: BOS
# WP: BOS #36 Junichi Tazawa
game.winning_pitcher(36)
# SV: BOS #40 Andrew Bailey
game.save_pitcher(40)

# Loser team: CLE
# LP: CLE #52 Vinnie Pestano
game.losing_pitcher(52, is_away_team=True)

# print(game)
game.generate_scorecard()
