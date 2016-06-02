$(function(){
    $('[data-input-mask]').each(function(){
        var input = $(this),
            opts = input.attr('data-input-mask').replace(/&quot;/g, '"'),
            opts = JSON.parse(opts),
            mask = opts.mask;

        delete opts.mask;

        opts.placeholder = input.attr('placeholder');

        $(this).mask(mask, opts);
    });

    $('[data-money-mask]').each(function(){
        var input = $(this),
            opts = input.attr('data-money-mask').replace(/&quot;/g, '"'),
            opts = JSON.parse(opts);

        $(this).maskMoney(opts).maskMoney('mask');
    });
});
