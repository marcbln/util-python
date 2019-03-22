# 03/2019 created
import json


class UtilJson:

    @classmethod
    def loadJsonFile(cls, pathJsonFile):
        with open(pathJsonFile) as f:
            data = json.load(f)
        return data


    # TODO: public static function saveJsonFile(string $pathJsonFile, $data, $options=JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE)



