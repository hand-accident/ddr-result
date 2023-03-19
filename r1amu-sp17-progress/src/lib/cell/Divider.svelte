<script>
    let className;
    export { className as class };
</script>

<div class="c0 {className}">
    <slot />
</div>

<style lang="postcss" module>
    .c0 {
        @apply divider text-xl;
    }
</style>
