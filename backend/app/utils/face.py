import cv2
import numpy as np
import face_recognition
from models.member import MemberTable as Member
from .mask import mask_check

import os


def face_check(img_path: str):
    # 비교할 이미지 로드
    img_path = "../img/cam_img/" + img_path
    img = face_recognition.load_image_file(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if len(face_recognition.face_locations(img)) == 0:
        return "얼굴인식 실패"

    user = face_recognition.face_encodings(img)[0]
    members = os.listdir('../img/member_img')

    for member in members:
        # 디비에 데이터를 가져와야함(임시 데이터 준형이 마스크얼굴)
        memberimg_path = "../img/member_img/" + member
        memberimg = face_recognition.load_image_file(memberimg_path)
        memberimg = cv2.cvtColor(memberimg, cv2.COLOR_BGR2RGB)

        # 기존 이용자 얼굴 분석
        memberface = face_recognition.face_encodings(memberimg)[0]

        # 얼굴 비교
        result = face_recognition.compare_faces([memberface], user)

        # 얼굴이 같으면 바로 리턴 하고 맴버정보 제공
        if result[0]:
            uuid_img = member
            return uuid_img

    return "등록된 회원이 아닙니다"
