import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-04-05
# https://www.baseball-reference.com/boxes/TOR/TOR201304050.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/04/05/346801/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-05 19:08-22:43",
        "at": "Rogers Centre, Toronto, ON",
        "att": "45,328",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                18: "Shane Victorino",
                44: "Jackie Bradley Jr.",
                10: "Jose Iglesias",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
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
                [29, "0"],
                [15, "4"],
                [12, "3"],
                [39, "2"],
                [16, "5"],
                [18, "9"],
                [44, "7"],
                [10, "6"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 30, 91, 52, 31, 59, 36, 11, 19, 46],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 55,
            "roster": {
                # Lineup
                7: "José Reyes",
                1: "Emilio Bonifácio",
                53: "Melky Cabrera",
                10: "Edwin Encarnación",
                9: "J.P. Arencibia",
                11: "Rajai Davis",
                28: "Colby Rasmus",
                16: "Mark DeRosa",
                3: "Maicer Izturis",
                # Starting pitcher
                55: "Josh Johnson",
                # Bench
                26: "Adam Lind",
                22: "Henry Blanco",
                19: "José Bautista",
                # Bullpen
                43: "R.A. Dickey",
                62: "Aaron Loup",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                38: "Darren Oliver",
                23: "Brandon Morrow",
                33: "Jeremy Jeffress",
                27: "Brett Cecil",
                21: "Sergio Santos",
                48: "J.A. Happ",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [62, 56, 38, 27, 48],
            "lineup": [
                [7, "6"],
                [1, "4"],
                [53, "7"],
                [10, "0"],
                [9, "2"],
                [11, "9"],
                [28, "8"],
                [16, "3"],
                [3, "5"],
            ],
            "bench": [
                [26, "1B"],
                [22, "C"],
                [19, "RF"],
            ],
            "bullpen": [43, 62, 50, 56, 38, 23, 33, 27, 21, 48, 44, 32],
        },
        "umpires": {
            "HP": "James Hoye",
            "1B": "John Hirschbeck",
            "2B": "Bob Davidson",
            "3B": "Jim Reynolds",
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
# Pitching: TOR #55 Josh Johnson
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b b")
t1.reach("BB")
t1.advance(2, "29 1B")
t1.advance(3, "15 F9")

# 2. BOS #29 Daniel Nava (X - X - 2)
t1.new_ab()
t1.pitch_list("b 1 c")
t1.hit(1)

# 3. BOS #15 Dustin Pedroia (X - 2 - 29)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("F9")

# 4. BOS #12 Mike Napoli (2 - X - 29)
t1.new_ab(is_risp=True)
t1.pitch_list("c b f 1 d s")
t1.out("K")

# 5. BOS #39 Jarrod Saltalamacchia (2 - X - 29)
t1.new_ab(is_risp=True)
t1.pitch_list("s f b b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.hit(2)
b1.advance(3, "53 WP")

# 2. TOR #1  Emilio Bonifácio (X - 7 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("l d s s")
b1.out("K")

# 3. TOR #53 Melky Cabrera (X - 7 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.wp()
b1.reach("FC5")
b1.thrown_out(2, "10 DP5-4-3", 2, 22)

# 4. TOR #10 Edwin Encarnación (7 - X - 53)
b1.new_ab(is_risp=True)
b1.pitch_list("b f s")
b1.out("DP5-4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #55 Josh Johnson
t2 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.out("P4")

# 7. BOS #18 Shane Victorino (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(3, "44 1B")
t2.advance(4, "2 1B")

# 8. BOS #44 Jackie Bradley Jr. (X - X - 18)
t2.new_ab()
t2.pitch_list("c 1 f")
t2.hit(1)
t2.advance(2, "10 HBP")
t2.advance(3, "2 1B")

# 9. BOS #10 Jose Iglesias (18 - X - 44)
t2.new_ab(is_risp=True)
t2.reach("HBP")
t2.advance(2, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (18 - 44 - 10)
t2.new_ab(is_risp=True)
t2.hit(1, rbis=1)
t2.thrown_out(2, "29 DP6-4-3", 2, 55)

# 2. BOS #29 Daniel Nava (44 - 10 - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("b s")
t2.out("DP6-4-3")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 5. TOR #9  J.P. Arencibia (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b f f")
b2.out("(F)P3")

# 6. TOR #11 Rajai Davis (X - X - X)
b2.new_ab()
b2.pitch_list("b f c")
b2.hit(1)
b2.advance(3, "28 2B")
b2.advance(4, "16 (F)SF9")

# 7. TOR #28 Colby Rasmus (X - X - 11)
b2.new_ab()
b2.hit(2)

# 8. TOR #16 Mark DeRosa (11 - 28 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("d c")
b2.out("(F)SF9", rbis=1)

# 9. TOR #3  Maicer Izturis (X - 28 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f f")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #55 Josh Johnson
t3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.out("F7")

# 4. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.out("(F)P3")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F7")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.thrown_out(2, "53 FC6-4", 2, 22)

# 2. TOR #1  Emilio Bonifácio (X - X - 7)
b3.new_ab()
b3.pitch_list("1 c b 1 1 s s")
b3.out("K")

# 3. TOR #53 Melky Cabrera (X - X - 7)
b3.new_ab()
b3.pitch_list("f b")
b3.reach("FC6-4")

# 4. TOR #10 Edwin Encarnación (X - X - 53)
b3.new_ab()
b3.pitch_list("f s d d 1 b c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #55 Josh Johnson
t4 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("c b b c f t")
t4.out("KT")

# 7. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.error(4)
t4.reach("E4")
t4.advance(2, "44 E4")
t4.advance("U", "23 1B")

# 8. BOS #44 Jackie Bradley Jr. (X - X - 18)
t4.new_ab()
t4.pitch_list("c 1")
t4.error(4)
t4.reach("E4")
t4.advance(2, "23 1B")

# Offensive change (BOS): Pinch-hitter #23 Pedro Ciriaco replaces #10 Jose Iglesias, batting 9th
t4.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Pedro Ciriaco (X - 18 - 44)
t4.new_ab(is_risp=True)
t4.pitch_list("d s s d")
t4.hit(1, rbis=1)

# 1. BOS #2  Jacoby Ellsbury (X - 44 - 23)
t4.new_ab(is_risp=True)
t4.pitch_list("b c s f f")
t4.out("IF4")

# 2. BOS #29 Daniel Nava (X - 44 - 23)
t4.new_ab(is_risp=True)
t4.out("L9")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# Defensive switch (BOS): #23 Pedro Ciriaco moves to SS
b4.defensive_switch(23, "6")

# 5. TOR #9  J.P. Arencibia (X - X - X)
b4.new_ab()
b4.pitch_list("b b f s f s")
b4.out("K")

# 6. TOR #11 Rajai Davis (X - X - X)
b4.new_ab()
b4.out("G4-3")

# 7. TOR #28 Colby Rasmus (X - X - X)
b4.new_ab()
b4.pitch_list("b c b s b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #55 Josh Johnson
t5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(1)
t5.advance(4, "12 HR")

# 4. BOS #12 Mike Napoli (X - X - 15)
t5.new_ab()
t5.pitch_list("d s")
t5.hit(4, rbis=2)

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("l s s")
t5.out("K2-3")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.out("G4-3")

# 7. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b b")
t5.hit(1)

# 8. BOS #44 Jackie Bradley Jr. (X - X - 18)
t5.new_ab()
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 8. TOR #16 Mark DeRosa (X - X - X)
b5.new_ab()
b5.pitch_list("f b b")
b5.hit(4)

# 9. TOR #3  Maicer Izturis (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b")
b5.hit(1)
b5.advance(4, "7 2B")

# 1. TOR #7  José Reyes (X - X - 3)
b5.new_ab()
b5.pitch_list("f f")
b5.hit(2, rbis=1)
b5.thrown_out(3, "7-5", 1, 22)

# 2. TOR #1  Emilio Bonifácio (X - X - X)
b5.new_ab()
b5.pitch_list("s")
b5.hit(1)

# 3. TOR #53 Melky Cabrera (X - X - 1)
b5.new_ab()
b5.pitch_list("b b")
b5.out("F9")

# 4. TOR #10 Edwin Encarnación (X - X - 1)
b5.new_ab()
b5.pitch_list("c b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #55 Josh Johnson
t6 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(2)

# 1. BOS #2  Jacoby Ellsbury (X - 23 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b b c c s")
t6.out("K")

# 2. BOS #29 Daniel Nava (X - 23 - X)
t6.new_ab(is_risp=True)
t6.out("P4")

# 3. BOS #15 Dustin Pedroia (X - 23 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b b i")
t6.reach("IBB")

# 4. BOS #12 Mike Napoli (X - 23 - 15)
t6.new_ab(is_risp=True)
t6.pitch_list("b b f b f c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #22 Felix Doubront
b6 = game.new_inning()

# 5. TOR #9  J.P. Arencibia (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b f f f")
b6.hit(2)

# Pitching change (BOS): #19 Koji Uehara replaces #22 Felix Doubront
b6.pitching_substitution(19)

# 6. TOR #11 Rajai Davis (X - 9 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("l b l t")
b6.out("KT")

# 7. TOR #28 Colby Rasmus (X - 9 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c s b s")
b6.out("K")

# Offensive change (TOR): Pinch-hitter #26 Adam Lind replaces #16 Mark DeRosa, batting 8th
b6.offensive_substitution(8, 26, "PH")

# 8. TOR #26 Adam Lind (X - 9 - X)
b6.new_ab(is_risp=True)
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #27 Brett Cecil
t7 = game.new_inning()

# Pitching change (TOR): #27 Brett Cecil replaces #55 Josh Johnson
t7.pitching_substitution(27)

# Defensive switch (TOR): #26 Adam Lind moves to 1B
t7.defensive_switch(26, "3")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.advance(3, "16 2B")

# 6. BOS #16 Will Middlebrooks (X - X - 39)
t7.new_ab()
t7.pitch_list("b c c")
t7.hit(2)

# 7. BOS #18 Shane Victorino (39 - 16 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c f s")
t7.out("K2-3")

# 8. BOS #44 Jackie Bradley Jr. (39 - 16 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b f c f s")
t7.out("K")

# 9. BOS #23 Pedro Ciriaco (39 - 16 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
b7.pitching_substitution(36)

# 9. TOR #3  Maicer Izturis (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("F8")

# 1. TOR #7  José Reyes (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(4)

# 2. TOR #1  Emilio Bonifácio (X - X - X)
b7.new_ab()
b7.pitch_list("l s s")
b7.out("K")

# 3. TOR #53 Melky Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("c c")
b7.hit(3)

# 4. TOR #10 Edwin Encarnación (53 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("t b b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #27 Brett Cecil
t8 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c f f b f s")
t8.out("K2-3")

# Pitching change (TOR): #32 Esmil Rogers replaces #27 Brett Cecil
t8.pitching_substitution(32)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #29 Daniel Nava, batting 2nd
t8.offensive_substitution(2, 5, "PH")

# 2. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b b")
t8.reach("BB")
t8.advance(3, "15 2B")
t8.advance(4, "12 G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t8.new_ab()
t8.pitch_list("c c")
t8.hit(2)

# 4. BOS #12 Mike Napoli (5 - 15 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b s s")
t8.out("G5-3", rbis=1)

# 5. BOS #39 Jarrod Saltalamacchia (X - 15 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c s d b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #40 Andrew Bailey
b8 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #36 Junichi Tazawa
b8.pitching_substitution(40)

# Defensive switch (BOS): #5 Jonny Gomes moves to DH
b8.defensive_switch(5, "0")

# 5. TOR #9  J.P. Arencibia (X - X - X)
b8.new_ab()
b8.pitch_list("f b s b s")
b8.out("K")

# 6. TOR #11 Rajai Davis (X - X - X)
b8.new_ab()
b8.pitch_list("f b")
b8.hit(2)
b8.advance(3, "26 F8")

# 7. TOR #28 Colby Rasmus (X - 11 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b s b b b")
b8.reach("BB")

# 8. TOR #26 Adam Lind (X - 11 - 28)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f")
b8.out("F8")

# 9. TOR #3  Maicer Izturis (11 - X - 28)
b8.new_ab(is_risp=True)
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #33 Jeremy Jeffress
t9 = game.new_inning()

# Pitching change (TOR): #33 Jeremy Jeffress replaces #32 Esmil Rogers
t9.pitching_substitution(33)

# 6. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(4)

# 7. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("f b s b f b b")
t9.reach("BB")
t9.advance(2, "23 SB")
t9.advance(3, "23 E4")
t9.thrown_out(4, "2 FC4-2", 2, 33)

# 9. BOS #23 Pedro Ciriaco (X - X - 44)
t9.new_ab(is_risp=True)
t9.pitch_list("c b s b")
t9.error(4)
t9.reach("E4")
t9.advance(2, "2 FC4-2")
t9.advance(3, "5 SB")

# 1. BOS #2  Jacoby Ellsbury (44 - X - 23)
t9.new_ab(is_risp=True)
t9.pitch_list("c f")
t9.reach("FC4-2")
t9.advance(2, "5 SB")

# 2. BOS #5  Jonny Gomes (X - 23 - 2)
t9.new_ab(is_risp=True)
t9.pitch_list("b c d b b")
t9.reach("BB")

# 3. BOS #15 Dustin Pedroia (23 - 2 - 5)
t9.new_ab(is_risp=True)
t9.pitch_list("b c b")
t9.out("F7")


# Bot 9th
# Pitching: BOS #52 Joel Hanrahan
b9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #40 Andrew Bailey
b9.pitching_substitution(52)

# 1. TOR #7  José Reyes (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c")
b9.out("(F)P5")

# 2. TOR #1  Emilio Bonifácio (X - X - X)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# 3. TOR #53 Melky Cabrera (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c f b")
b9.reach("BB")

# 4. TOR #10 Edwin Encarnación (X - X - 53)
b9.new_ab()
b9.pitch_list("b")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #36 Junichi Tazawa
game.winning_pitcher(36, is_away_team=True)
# SV: BOS #52 Joel Hanrahan
game.save_pitcher(52, is_away_team=True)

# Loser team: TOR
# LP: TOR #32 Esmil Rogers
game.losing_pitcher(32)

# print(game)
game.generate_scorecard()
