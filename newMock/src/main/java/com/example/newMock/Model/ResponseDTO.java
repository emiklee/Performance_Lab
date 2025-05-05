package com.example.newMock.Model;


import lombok.AllArgsConstructor;
import lombok.Data;

import java.math.BigDecimal;

@Data
@AllArgsConstructor

public class ResponseDTO {
    private String rqUID;
    private String clientId;
    private String account;
    private String currency;
    private float balance;
    private BigDecimal maxLimit;
}
