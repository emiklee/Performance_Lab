package com.example.newMock.Controller;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.example.newMock.Model.RequestDTO;
import com.example.newMock.Model.ResponseDTO;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.coyote.Request;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import java.util.Random;
import javax.print.attribute.standard.MediaTray;
import java.awt.*;
import java.math.BigDecimal;

@RestController
public class MainController {

    private Logger log = LoggerFactory.getLogger(MainController.class);
    ObjectMapper mapper = new ObjectMapper();
    Random random = new Random();


    @PostMapping(
            value = "/info/postBalances",
            produces = MediaType.APPLICATION_JSON_VALUE,
            consumes = MediaType.APPLICATION_JSON_VALUE
    )
    public Object postBalances(@RequestBody RequestDTO requestDTO) {
        try {
            String clientUID = requestDTO.getClientId();
            char firstChar = clientUID.charAt(0);
            int maxLimit = 10000;
            String currency = "RUB";
            if (firstChar == '8') {
                maxLimit = 2000;
                currency = "US";
            }
            else if (firstChar == '9') {
                maxLimit = 1000;
                currency = "EU";
            }
            float balance = random.nextInt(maxLimit * 100) / 100f;
            System.out.println(balance);
            ResponseDTO responseDTO = new ResponseDTO(requestDTO.getRqUID(), requestDTO.getClientId(),
                    requestDTO.getAccount(), currency, balance, BigDecimal.valueOf(maxLimit));

            log.error("****** RequestDTO *******" + mapper.writerWithDefaultPrettyPrinter().writeValueAsString(requestDTO));
            log.error("****** RequestDTO *******" + mapper.writerWithDefaultPrettyPrinter().writeValueAsString(responseDTO));

            return responseDTO;

        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }
    }
}

